from django.db import models


class LoginRecord(models.Model):

    user = models.CharField(default='', max_length=30)


class ServerUser(models.Model):

    pass
