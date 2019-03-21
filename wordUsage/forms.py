from django import forms

class ContactForm(forms.Form):
    t1 = forms.CharField(label='first term', max_length=100)
    t2 = forms.CharField(label='second term', max_length=100)
    t3 = forms.CharField(label='third term', max_length=100)
    start_mo = forms.CharField(label='start month', max_length=2)
    start_yr = forms.CharField(label='start year', max_length=4)
    end_mo = forms.CharField(label='end month', max_length=2)
    end_yr = forms.CharField(label='end year', max_length=4)