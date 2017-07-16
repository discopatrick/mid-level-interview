from django.test import TestCase
from .models import LoginRecord, ServerUser


class LoginRecordTestCase(TestCase):

    def test_relate_loginrecord_to_serveruser(self):
        user = ServerUser.objects.create(username='patrick')
        login_record = LoginRecord.objects.create(server_user=user)
        retrieved_login_record = LoginRecord.objects.get(pk=login_record.pk)

        self.assertEqual(retrieved_login_record.server_user, user)


class ServerUserTestCase(TestCase):

    def test_create_user(self):
        user = ServerUser.objects.create(username='patrick')
        retrieved_user = ServerUser.objects.get(pk=user.pk)

        self.assertEqual(retrieved_user.username, 'patrick')
