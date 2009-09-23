from django import forms

class CommentForm(forms.Form):
    author = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)