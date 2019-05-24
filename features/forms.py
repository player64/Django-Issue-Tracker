from django import forms
from .models import Features, FeatureComment


class FeatureForm(forms.ModelForm):

    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Features
        fields = ['name', 'description']


class FeatureCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = FeatureComment
        fields = ['comment']
