from django import forms
from .models import Features, FeatureComment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit comment'))