from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation 
from .models import Customer
class custumerRegisterForm(UserCreationForm):
    #password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #password2=forms.CharField(label='confirm pass',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #Email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widget={
            'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username=UsernameField(label=('username'),widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=('password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))       

class passwordForm(PasswordChangeForm):
    oldpassword=forms.CharField(label=('oldpassword'),widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    newpassword1=forms.CharField(label=('new1password'),widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    newpassword2=forms.CharField(label=('new2password'),widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
class passwordReset(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class profileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','zipcode','state']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-controll'}),
            'locality':forms.TextInput(attrs={'class':'form-controll'}),
            'city':forms.TextInput(attrs={'class':'form-controll'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-controll'}),
            'state':forms.Select(attrs={'class':'form-controll'})
        }