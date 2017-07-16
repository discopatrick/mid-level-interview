import csv

from django.core.management import BaseCommand

from monitoring.models import LoginRecord


class Command(BaseCommand):

    USERNAME_INDEX = 3

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        login_records_created = 0

        with open(options['file']) as f:
            reader = csv.reader(f)
            for row in reader:
                LoginRecord.objects.create(user=row[self.USERNAME_INDEX])
                login_records_created += 1

        self.stdout.write("{} login records created.".format(
                          login_records_created))
