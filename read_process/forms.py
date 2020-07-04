from django import forms


class readForm(forms.Form):
    keyword = forms.CharField(max_length=100)
    process = forms.CharField(max_length=100)

    