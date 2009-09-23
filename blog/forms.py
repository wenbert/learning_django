from django import forms
import datetime

class CommentForm(forms.Form):
    author = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField(initial=datetime.date.today);