from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'phone_number', 'bank', 'bankAccount']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        password_confirm = cleaned_data.get("password2")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['roadAddress', 'jibunAddress', 'extraAddress', 'detailAddress','postcode']
        widgets = {
            'roadAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'jibunAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'extraAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'detailAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
        }