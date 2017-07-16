from django.db import models


class ServerUser(models.Model):

    username = models.CharField(default='', max_length=30)


class LoginRecord(models.Model):

    server_user = models.ForeignKey(ServerUser)
    datetime = models.DateTimeField()
