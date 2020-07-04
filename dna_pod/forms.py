from django import forms

class DNAForm(forms.Form):
    patterns = forms.CharField(max_length=100)
    ref_text = forms.CharField(max_length=100)
    method = forms.CharField(max_length=100)


    