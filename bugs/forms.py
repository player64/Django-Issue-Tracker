from django import forms
from .models import Bugs, BugComment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BugForm(forms.ModelForm):

    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Bugs
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Edit bug'))


class BugCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = BugComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit comment'))
