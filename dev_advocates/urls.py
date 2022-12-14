"""dev_advocates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    """
    Welcome to My implementation of the Agora october hackathon.
    Hackathon details: https://codebattles.dev/event/dce4b8cd-b48d-4511-b4d6-b0058c179944/
    Github: https://github.com/itslewisndungu/codebattles-october-hackathon

    Sample login details:
        Username: admin
        Password: supercooladminpassword
    """
    return Response(
        {
            "advocates": reverse(
                "advocates:list-create", request=request, format=format
            ),
        }
    )


urlpatterns = [
    path("", api_root),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path("advocates/", include("advocates.urls", namespace="advocates")),
]
