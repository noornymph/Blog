"""This module contains forms of our django app."""

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """This class represents the structure of the form."""

    class Meta:
        """This class represents the structure of the post."""

        model = Post
        fields = (
            "title",
            "text",
        )
