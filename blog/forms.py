from django import forms
import datetime

class CommentForm(forms.Form):
    author = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)