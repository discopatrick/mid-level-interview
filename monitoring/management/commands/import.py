import csv

from django.core.management import BaseCommand

from monitoring.models import LoginRecord, ServerUser


class Command(BaseCommand):

    USERNAME_INDEX = 3

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        login_records_created = 0
        server_users_created = 0

        with open(options['file']) as f:
            reader = csv.reader(f)
            for row in reader:
                username = row[self.USERNAME_INDEX]
                server_user, created = ServerUser.objects.get_or_create(
                    username=username)
                if created:
                    server_users_created += 1
                LoginRecord.objects.create(server_user=server_user)
                login_records_created += 1

        self.stdout.write("{} new server users created.".format(
                          server_users_created))
        self.stdout.write("{} login records created.".format(
                          login_records_created))
