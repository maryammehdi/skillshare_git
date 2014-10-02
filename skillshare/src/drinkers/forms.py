from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from drinkers.models import Drinker


class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'User name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    
    class Meta:
        model = Drinker
        exclude = ('USer',)
        
    def clean_username(self):
        username = self.cleaned_data['username']
        
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        return forms.ValidateError("that username is already taken, please select another.")
    
    def clean_password(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise forms.ValidationError("Passwords did cnot match, please try again.")
        return password