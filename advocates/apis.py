from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

advocates = {
    "advocates": [
        {
            "profile_pic": "https://pbs.twimg.com/profile_images/1489066537407365126/iViPGBVE_400x400.jpg",
            "username": "dennisivy11",
            "name": "Dennis Ivy",
            "bio": "YouTuber, contributor at @traversymedia , developer advocate @agoraio and online instructor.",
            "twitter": "https://twitter.com/dennisivy11",
        },
    ]
}

advocate = {
    "profile_pic": "https://pbs.twimg.com/profile_images/1489066537407365126/iViPGBVE_400x400.jpg",
    "username": "dennisivy11",
    "name": "Dennis Ivy",
    "bio": "YouTuber, contributor at @traversymedia , developer advocate @agoraio and online instructor.",
    "twitter": "https://twitter.com/dennisivy11",
}


class AdvocatesListApi(APIView):
    def get(self, request):
        return Response(advocates)


class AdvocateRetrieveApi(APIView):
    def get(self, request, id: str):
        return Response(advocate)
