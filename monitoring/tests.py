from django.test import TestCase
from .models import LoginRecord


class LoginRecordTestCase(TestCase):

    def test_create_loginrecord(self):
        login_record = LoginRecord.objects.create()
        login_record.user = 'patrick'
        login_record.save()
        retrieved_login_record = LoginRecord.objects.get(pk=login_record.pk)

        self.assertEqual(retrieved_login_record.user, 'patrick')
