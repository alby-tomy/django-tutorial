from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    Converts the Member model into JSON for DRF endpoints.
    This is the data layer used by the CRUD API.
    """

    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']