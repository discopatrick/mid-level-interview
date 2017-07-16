from django.test import TestCase
from .models import LoginRecord

class LoginRecordTestCase(TestCase):

    def test_create_loginrecord(self):
        login_record = LoginRecord.objects.create()
        login_record.save()
