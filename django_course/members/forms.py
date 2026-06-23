from django import forms

from .models import Member
from .validators import EMAIL_INVALID_MESSAGE


class MemberForm(forms.ModelForm):
    """
    contact_number's format validation lives on the model field
    (see validators.validate_contact_number) so it also applies in
    the admin and on Member.full_clean(), not just here.
    """

    class Meta:
        model = Member
        fields = ['name', 'age', 'email', 'contact_number', 'address', 'social_media_url', 'profile_image']
        error_messages = {
            'email': {
                'invalid': EMAIL_INVALID_MESSAGE,
                'unique': 'A member with this email already exists.',
            },
        }
