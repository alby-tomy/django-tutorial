from django.test import TestCase
from django.urls import reverse

from .forms import MemberForm
from .models import Member
from .validators import EMAIL_INVALID_MESSAGE


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


class MemberFormTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(name='Bob', email='bob@example.com')

    def valid_data(self, **overrides):
        data = {
            'name': 'Bob',
            'age': 30,
            'email': 'bob@example.com',
            'contact_number': '+1234567890',
            'address': '',
            'social_media_url': '',
        }
        data.update(overrides)
        return data

    def test_valid_data_is_accepted(self):
        form = MemberForm(data=self.valid_data(), instance=self.member)
        self.assertTrue(form.is_valid(), form.errors)

    def test_malformed_contact_number_is_rejected(self):
        form = MemberForm(data=self.valid_data(contact_number='abc'), instance=self.member)
        self.assertFalse(form.is_valid())
        self.assertIn('contact_number', form.errors)

    def test_malformed_email_is_rejected(self):
        form = MemberForm(data=self.valid_data(email='not-an-email'), instance=self.member)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], EMAIL_INVALID_MESSAGE)

    def test_duplicate_email_is_rejected(self):
        Member.objects.create(name='Carol', email='carol@example.com')
        form = MemberForm(data=self.valid_data(email='carol@example.com'), instance=self.member)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class MemberUpdateViewTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(name='Bob', email='bob@example.com')
        self.url = reverse('member_update', args=[self.member.pk])

    def test_get_renders_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="contact_number"')

    def test_post_with_invalid_contact_number_reshows_form_with_error(self):
        response = self.client.post(self.url, {
            'name': 'Bob', 'age': 30, 'email': 'bob@example.com',
            'contact_number': 'xyz', 'address': '', 'social_media_url': '',
        })
        self.assertEqual(response.status_code, 200)  # re-rendered, not redirected
        self.assertContains(response, 'Enter a valid contact number')
        self.member.refresh_from_db()
        self.assertEqual(self.member.contact_number, '')  # unchanged

    def test_post_with_valid_data_saves_and_redirects(self):
        response = self.client.post(self.url, {
            'name': 'Bob', 'age': 30, 'email': 'bob@example.com',
            'contact_number': '+1234567890', 'address': '', 'social_media_url': '',
        })
        self.assertRedirects(response, reverse('member_detail_view', args=[self.member.pk]))
        self.member.refresh_from_db()
        self.assertEqual(self.member.contact_number, '+1234567890')
