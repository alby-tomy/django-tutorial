from django.test import TestCase
from django.urls import reverse

from .models import Member


class MemberCrudApiTest(TestCase):
    def test_member_list_api_returns_200(self):
        response = self.client.get(reverse('member_list'))
        self.assertEqual(response.status_code, 200)

    def test_member_create_api_creates_member(self):
        response = self.client.post(
            reverse('member_list'),
            {'name': 'Alice', 'email': 'alice@example.com'},
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Member.objects.filter(email='alice@example.com').exists())
