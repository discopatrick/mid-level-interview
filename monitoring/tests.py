from django.test import TestCase
from django.utils import timezone

from .models import LoginRecord, ServerUser, Server


class LoginRecordTestCase(TestCase):

    def test_create_loginrecord(self):
        user = ServerUser.objects.create(username='patrick')
        server = Server.objects.create(ip='10.10.10.10')
        login_record = LoginRecord.objects.create(
            server_user=user,
            server=server,
            datetime=timezone.now()
        )
        retrieved_login_record = LoginRecord.objects.get(pk=login_record.pk)

        self.assertEqual(retrieved_login_record.server_user, user)
        self.assertEqual(retrieved_login_record.server, server)

    def test_add_datetime_to_loginrecord(self):

        user = ServerUser.objects.create(username='patrick')
        server = Server.objects.create(ip='10.10.10.10')
        login_record = LoginRecord.objects.create(
            server_user=user,
            datetime=timezone.now(),
            server=server
        )
        retrieved_login_record = LoginRecord.objects.get(pk=login_record.pk)

        self.assertEqual(
            retrieved_login_record.datetime,
            login_record.datetime
        )


class ServerUserTestCase(TestCase):

    def test_create_user(self):
        user = ServerUser.objects.create(username='patrick')
        retrieved_user = ServerUser.objects.get(pk=user.pk)

        self.assertEqual(retrieved_user.username, 'patrick')

    def test_add_contact_info_to_user(self):
        user = ServerUser.objects.create(username='patrick')
        user_email_address = 'example@example.com'
        user.add_contact_info(user_email_address)

        self.assertEqual(user.email, user_email_address)


class ServerTestCase(TestCase):

    def test_create_server(self):
        server = Server.objects.create(ip='255.255.255.255')
        retrieved_server = Server.objects.get(pk=server.pk)

        self.assertEqual(retrieved_server.ip, '255.255.255.255')
