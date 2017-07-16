import re

from django.db import models


class ServerUser(models.Model):

    EMAIL_REGEX = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    username = models.CharField(default='', max_length=30)
    email = models.EmailField(null=True, blank=True)
    # TODO: add phone number field

    def add_contact_info(self, info):
        if self.EMAIL_REGEX.match(info):
            self.email = info
            
        # TODO: also handle when info matches a phone number

        self.save()


class Server(models.Model):

    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=30)


class LoginRecord(models.Model):

    server_user = models.ForeignKey(ServerUser)
    datetime = models.DateTimeField()
    server = models.ForeignKey(Server)
