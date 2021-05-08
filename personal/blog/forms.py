from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class SendMail(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
