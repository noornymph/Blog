"""This module represents the model of the blog post"""

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """This class represents the model of our blog"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()

    def publish(self):
        """This function manages the publishing time and date"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)
