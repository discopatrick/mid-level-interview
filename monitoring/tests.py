from django.test import TestCase
from .models import LoginRecord, ServerUser


class LoginRecordTestCase(TestCase):

    def test_create_loginrecord(self):
        login_record = LoginRecord.objects.create()
        login_record.user = 'patrick'
        login_record.save()
        retrieved_login_record = LoginRecord.objects.get(pk=login_record.pk)

        self.assertEqual(retrieved_login_record.user, 'patrick')


class ServerUserTestCase(TestCase):

    def test_create_user(self):
        user = ServerUser.objects.create(username='patrick')
        retrieved_user = ServerUser.objects.get(pk=user.pk)

        self.assertEqual(retrieved_user.username, 'patrick')
