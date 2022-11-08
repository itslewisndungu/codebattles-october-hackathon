from django.urls import path
from .apis import AdvocateRetrieveApi, AdvocatesListApi


urlpatterns = [
    path("", AdvocatesListApi.as_view()),
    path("<str:username>/", AdvocateRetrieveApi.as_view()),
]
