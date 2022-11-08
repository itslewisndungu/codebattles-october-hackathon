from rest_framework import serializers
from .models import Advocate
from rest_framework.validators import UniqueValidator


class AdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ["profile_pic", "name", "twitter", "username", "bio"]
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
