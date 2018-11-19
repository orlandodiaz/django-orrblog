
from django.forms import ModelForm
from django.forms import CharField, Textarea
from markdownx.fields import MarkdownxFormField
from .models import Page
from django import forms


class UpdatePageForm(ModelForm):
    title = CharField(max_length=100)
    # body = CharField(max_length=2000, widget=Textarea)
    body = MarkdownxFormField()

    class Meta:
        model = Page
        fields = ['body']




    # def get_initial(self):
    #     """
    #     Returns the initial data to use for forms on this view.
    #     """
    #     initial = super(UpdatePageForm, self).get_initial()
    #
    #     initial['body'] = 'lolwut'
    #
    #     return initial