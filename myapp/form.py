from django import forms
class customform(forms.Form):
    username=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(max_length=100)