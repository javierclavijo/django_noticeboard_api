from django.test import TestCase
from django.urls import reverse
from .models import Notice
import datetime
from django.utils import timezone


# Create your tests here.
class ActiveNoticesViewTest(TestCase):
    def test_no_notices(self):
        response = self.client.get(reverse('noticeboard:active-notices'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No notices yet.')
        self.assertQuerysetEqual(response.context['active_notices_list'], [])

    def test_active_notice(self):
        Notice.objects.create(title='Achus', pub_date=timezone.now(),
                              exp_date=timezone.now() + datetime.timedelta(days=1), body='Achus 123')
        response = self.client.get(reverse('noticeboard:active-notices'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Achus')
        self.assertQuerysetEqual(response.context['active_notices_list'], ['<Notice: Achus>'])

    def test_expired_notice(self):
        Notice.objects.create(title='Achus', pub_date=timezone.now(),
                              exp_date=timezone.now() - datetime.timedelta(days=1), body='Achus 123')
        response = self.client.get(reverse('noticeboard:active-notices'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['active_notices_list'], [])
