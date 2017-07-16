from django.db import models


class ServerUser(models.Model):

    username = models.CharField(default='', max_length=30)

    def add_contact_info(self, info):
        pass


class LoginRecord(models.Model):

    server_user = models.ForeignKey(ServerUser)
    datetime = models.DateTimeField()
