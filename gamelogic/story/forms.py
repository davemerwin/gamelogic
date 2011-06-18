from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from gamelogic.story.models import Story

class StoryEditForm(ModelForm):
    class Meta:
        model = Story
        exclude = ('created','modified')