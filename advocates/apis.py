from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, GenericAPIView
from .models import Advocate
from .serializers import AdvocatesSerializer


class AdvocatesListApi(GenericAPIView):
    """
    Get a list of all advocates registered
    """

    serializer_class = AdvocatesSerializer
    queryset = Advocate.objects.all()

    search_fields = ["username", "bio", "twitter", "name"]

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AdvocateRetrieveApi(GenericAPIView):
    """
    Retrieve an advocate through the username
    """

    serializer_class = AdvocatesSerializer
    queryset = Advocate.objects.all()

    def get(self, _, username: str):
        advocate = get_object_or_404(self.get_queryset(), username=username)
        serializer = self.get_serializer(advocate)
        return Response(serializer.data)
