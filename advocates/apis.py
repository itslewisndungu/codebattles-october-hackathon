from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.generics import get_object_or_404, GenericAPIView
from .models import Advocate
from .serializers import AdvocatesSerializer
from rest_framework import filters


class AdvocatesListApi(GenericAPIView):
    """
    Get a list of all advocates registered
    """

    serializer_class = AdvocatesSerializer
    queryset = Advocate.objects.all()

    filterset_fields = ["username"]
    search_fields = ["username", "bio", "twitter", "name"]

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        res = {
            "advocates": serializer.data,
        }

        return Response(res)


class AdvocateRetrieveApi(GenericAPIView):
    def get(self, request, id: str):
        qs = Advocate.objects.all()
        advocate = get_object_or_404(qs, id=id)

        data = self.OutputSerializer(advocate).data
        return Response(data)
