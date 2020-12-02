from django.contrib.auth.models import User 

from django import forms

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-field form-group col-md-5 bg-light', 'placeholder':"Enter Your Password.."}))

    class Meta:
        model = User 
        
        fields = ['first_name', 'last_name','username', 'password']
        help_texts = {
            'username':None
        }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-field form-group col-md-5 bg-light', 'placeholder':"Enter Your User Name.."}),
            'first_name':forms.TextInput(attrs={'class':'form-field form-group col-md-5 bg-light', 'placeholder':"Enter Your First Name.." }),
            'last_name':forms.TextInput(attrs={'class':'form-field form-group col-md-5 bg-light', 'placeholder':"Enter Your Last Name.." }),
        }