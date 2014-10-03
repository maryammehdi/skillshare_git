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
        exclude = ('User',)
        
    def clean_username(self):
        username = self.cleaned_data['username']
        
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("that username is already taken, please select another.")
    
    def clean(self):
        print self.cleaned_data
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not match. Please try again.")
        return self.cleaned_data