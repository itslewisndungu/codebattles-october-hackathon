from rest_framework import serializers
from .models import Advocate


class AdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ["profile_pic", "name", "twitter", "username", "bio"]
