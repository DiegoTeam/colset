from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Profile
        fields = ["about", "experience", "education", "first_name", "last_name"]
