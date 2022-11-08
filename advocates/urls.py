from django.urls import path
from .apis import AdvocateRetrieveUpdateDeleteApi, AdvocatesListCreateApi


urlpatterns = [
    path("", AdvocatesListCreateApi.as_view()),
    path("<str:username>/", AdvocateRetrieveUpdateDeleteApi.as_view()),
]
