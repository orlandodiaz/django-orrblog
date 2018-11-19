
from django.forms import ModelForm
from django.forms import CharField, Textarea
from markdownx.fields import MarkdownxFormField
from .models import Page, Post
from django import forms


class UpdatePageForm(ModelForm):
    title = CharField(max_length=100)
    # body = CharField(max_length=2000, widget=Textarea)
    body2 = MarkdownxFormField()

    class Meta:
        model = Page
        fields = ['body2']


class UpdatePostForm(ModelForm):
    title = CharField(max_length=100)
    # body = CharField(max_length=2000, widget=Textarea)
    body2 = MarkdownxFormField()

    class Meta:
        model = Post
        fields = ['body2']

    # def get_initial(self):
    #     """
    #     Returns the initial data to use for forms on this view.
    #     """
    #     initial = super(UpdatePageForm, self).get_initial()
    #
    #     initial['body'] = 'lolwut'
    #
    #     return initial