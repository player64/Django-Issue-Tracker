from django import forms
from .models import Bugs, BugComment


class BugForm(forms.ModelForm):

    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Bugs
        fields = ['name', 'description']


class BugCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = BugComment
        fields = ['comment']
