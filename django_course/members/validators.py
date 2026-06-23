import re

from django.core.exceptions import ValidationError

CONTACT_NUMBER_REGEX = re.compile(r'^\+?\d{7,15}$')
CONTACT_NUMBER_INVALID_MESSAGE = 'Enter a valid contact number: 7-15 digits, optionally starting with "+".'
EMAIL_INVALID_MESSAGE = 'Enter a valid email address, e.g. name@example.com.'


class InvalidContactNumberError(ValidationError):
    """Raised when a contact number isn't 7-15 digits (optionally prefixed with '+')."""

    def __init__(self):
        super().__init__(CONTACT_NUMBER_INVALID_MESSAGE, code='invalid_contact_number')


def validate_contact_number(value):
    """Field validator — attach to a model/form field to enforce the contact number format."""
    if value and not CONTACT_NUMBER_REGEX.match(value.strip()):
        raise InvalidContactNumberError()
