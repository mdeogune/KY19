from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.auth.password_validation import validate_password
from allauth.account.forms import ResetPasswordForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import filter_users_by_email

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import KYProfile

class MyResetPasswordForm(ResetPasswordForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = filter_users_by_email(email)
        if not len(self.users):
            raise forms.ValidationError(_("The e-mail address is not assigned"
                                          " to any user account"))

        elif len(self.users[0].socialaccount_set.filter(provider='facebook')):
            raise forms.ValidationError(_("You are using a social account to login you can't reset password."))
        return self.cleaned_data["email"]





class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = KYProfile
        fields = ('full_name', 'email')
