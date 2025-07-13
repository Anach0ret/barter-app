from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter username/email', 'class': 'text_small_light'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'text_small_light'}),
    )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'font-secondary'
        }),
        min_length=8,
        error_messages={'min_length': 'Password must be at least 8 characters long.'}
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'font-secondary'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'city', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username',
                'class': 'font-secondary',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email',
                'class': 'font-secondary',
                'required': True
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter city',
                'class': 'font-secondary'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        return username


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'text_small_light',
            'placeholder': 'Enter your email'
        })
    )

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'placeholder': 'Enter new password',
            'class': 'text_small_light',
            'required': '',
        })
        self.fields['new_password2'].widget.attrs.update({
            'placeholder': 'Confirm new password',
            'class': 'text_small_light',
            'required': '',
        })