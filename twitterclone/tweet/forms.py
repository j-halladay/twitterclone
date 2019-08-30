from django import forms


class CreateTweet(forms.Form):
    text = forms.CharField(max_length=140)
