from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        form = CollaborateForm({
            'name': 'Tester',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_email_is_required(self):
        form = CollaborateForm({
            'name': 'Tester',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        form = CollaborateForm({
            'name': 'tester',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
