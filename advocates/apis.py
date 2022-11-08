from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, GenericAPIView
from .models import Advocate
from .serializers import AdvocatesSerializer
from rest_framework.request import Request
from rest_framework import status


class AdvocatesListCreateApi(GenericAPIView):
    """
    Get a list of all advocates registered
    """

    serializer_class = AdvocatesSerializer
    queryset = Advocate.objects.all()

    search_fields = ["username", "bio", "twitter", "name"]

    def get(self, request: Request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Advocate.objects.create(**serializer.data)

        return Response(serializer.data, status.HTTP_201_CREATED)


class AdvocateRetrieveUpdateDeleteApi(GenericAPIView):
    """
    Retrieve or update an advocate through the username
    """

    serializer_class = AdvocatesSerializer
    queryset = Advocate.objects.all()
    lookup_field = "username"

    def get(self, request, username: str):
        advocate = self.get_object()
        serializer = self.get_serializer(advocate)
        return Response(serializer.data)

    def post(self, request, username):
        advocate = self.get_object()

        serializer = self.get_serializer(
            advocate,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object()

        serializer = self.get_serializer(
            advocate,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, username):
        advocate = self.get_object()
        advocate.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
