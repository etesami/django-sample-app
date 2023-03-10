from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    
    
    def clean_renewal_date(self):
        your_name = self.cleaned_data['your_name']
        return your_name