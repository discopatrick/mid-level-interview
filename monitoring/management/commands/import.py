import csv
from datetime import datetime

from django.core.management import BaseCommand

from monitoring.models import LoginRecord, ServerUser, Server


class Command(BaseCommand):

    help = 'Imports the specified CSV file'

    SERVER_NAME_INDEX = 0
    SERVER_IP_INDEX = 1
    USERNAME_INDEX = 2
    CONTACT_INDEX = 4
    DATETIME_INDEX = 5

    DATETIME_FORMATS = [
        '%Y-%m-%d %H:%M:%S.%f',  # ISO formatted datetime
        '%Y-%m-%d',  # ISO formatted date

        # other date formats in the CSV
        '%y/%m/%d',
        '%y/%d/%m',
        '%m/%d/%y',
        '%d\\%m\\%y',
        '%y\\%m\\%d',
        '%m\\%d\\%y',
        '%d\\%y\\%m',
        '%m|%d|%y',
        '%d|%m|%y',
        '%y|%d|%m',
    ]

    def add_arguments(self, parser):
        parser.add_argument('file')


    def handle(self, *args, **options):
        """
        TODO: there is too much code in this function.
        Separate out into helper functions, or into a reusable library.
        """

        login_records_created = 0
        server_users_created = 0
        servers_created = 0

        with open(options['file']) as f:
            reader = csv.reader(f)
            first_line = True

            # TODO: Handle when two consecutive rows represent a single login.

            for row in reader:
                if first_line:
                    first_line = False
                    continue

                username = row[self.USERNAME_INDEX]
                raw_login_datetime = row[self.DATETIME_INDEX]

                parsed_datetime = None

                for format in self.DATETIME_FORMATS:
                    try:
                        parsed_datetime = datetime.strptime(raw_login_datetime,
                                                            format)
                        break
                    except ValueError as e:
                        # couldn't parse datetime
                        pass

                if parsed_datetime is None:
                    print('failed to parse {}'.format(raw_login_datetime))
                    continue

                server_user, user_created = ServerUser.objects.get_or_create(
                    username=username)
                if user_created:
                    server_users_created += 1

                contact_info = row[self.CONTACT_INDEX]
                server_user.add_contact_info(contact_info)

                server, server_created = Server.objects.get_or_create(
                    ip=row[self.SERVER_IP_INDEX]
                )
                if server_created:
                    servers_created += 1

                server_name = row[self.SERVER_NAME_INDEX].strip()
                if server_name:
                    server.name = server_name
                    server.save()

                LoginRecord.objects.create(server_user=server_user,
                                           datetime=parsed_datetime,
                                           server=server)
                login_records_created += 1

        self.stdout.write("{} new server users created.".format(
                          server_users_created))
        self.stdout.write("{} new servers created.".format(
                          servers_created))
        self.stdout.write("{} login records created.".format(
                          login_records_created))
