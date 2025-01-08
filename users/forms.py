from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'phone_number', 'bank', 'bankaccount']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['roadAddress', 'jibunAddress', 'postcode']
        widgets = {
            'roadAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'jibunAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
        }