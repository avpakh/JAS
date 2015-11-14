from django import forms

class PostLevelForm(forms.Form):
    content = forms.FloatField()
