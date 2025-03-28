from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Address


class CustomUserCreationForm(UserCreationForm):
    marketing_agree = forms.BooleanField(
        required=False,
        label="마케팅 수신 동의"
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'name',
            'phone_number',
            'bank',
            'bankAccount',
            'marketing_agree',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("이미 사용 중인 이메일입니다.")
        return email


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'postcode',
            'roadAddress',
            'jibunAddress',
            'extraAddress',
            'detailAddress'
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'name',
            'phone_number',
            'bank',
            'bankAccount',
            'marketing_agree',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("이미 사용 중인 이메일입니다.")
        return email
