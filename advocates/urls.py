from django.urls import path
from .apis import AdvocateRetrieveUpdateDeleteApi, AdvocatesListCreateApi

app_name="advocates"
urlpatterns = [
    path("", AdvocatesListCreateApi.as_view(), name="list-create"),
    path(
        "<str:username>/",
        AdvocateRetrieveUpdateDeleteApi.as_view(),
        name="retrieve-update-delete",
    ),
]
