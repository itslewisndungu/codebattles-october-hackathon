from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from .models import Advocate


class AdvocatesListApi(APIView):
    """
    Get a list of all advocates registered
    """

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Advocate
            fields = ["profile_pic", "name", "twitter", "username", "bio"]

    def get(self, request):
        qs = Advocate.objects.all()
        data = self.OutputSerializer(qs, many=True).data
        return Response(data)


class AdvocateRetrieveApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Advocate
            fields = ["profile_pic", "name", "twitter", "username", "bio"]

    def get(self, request, id: str):
        qs = Advocate.objects.all()
        advocate = get_object_or_404(qs, id=id)

        data = self.OutputSerializer(advocate).data
        return Response(data)
