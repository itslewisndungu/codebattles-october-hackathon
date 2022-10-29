from django.db import models


class Advocate(models.Model):
    profile_pic = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    twitter = models.CharField(max_length=60)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.username}"
