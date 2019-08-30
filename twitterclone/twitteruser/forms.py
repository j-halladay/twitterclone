from django import forms


class AddUser(forms.Form):
    username = forms.CharField(max_length=30)
    name = forms.CharField(max_length=40)
    bio = forms.CharField(max_length=150)

    password = forms.CharField(widget=forms.PasswordInput)
