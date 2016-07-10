from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from accounts.models import User


USERNAME_RE = r'^[\.\w]+$'


class SignupForm(forms.Form):
    """
    Form for creating a new user account.
    Validates that the requested username and e-mail is not already in use.
    Also requires the password to be entered twice.
    """
    username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})
    email = forms.EmailField(label=_("Email"))
    password1 = forms.CharField(label=_("Create password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_("Repeat password"), widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'usersignup'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        """
        Validates that the values entered into the two password fields match.
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('The two password fields didn\'t match.'))
        return self.cleaned_data

    def clean_username(self):
        try:
            user = get_user_model().objects.get(username__iexact=self.cleaned_data['username'])
        except get_user_model().DoesNotExist:
            pass
        else:
            raise forms.ValidationError(_('This username is already taken.'))
        return self.cleaned_data['username']

    def clean_email(self):
        if get_user_model().objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_('This email is already in use. Please supply a different email.'))
        return self.cleaned_data['email']

    def save(self):
        username, email, password = (self.cleaned_data['username'],
                                     self.cleaned_data['email'],
                                     self.cleaned_data['password1'])
        new_user = User.objects.create_user(username,
                                            email,
                                            password)
        # login(request, user)
        return new_user


class SignInForm(forms.Form):
    identification = forms.CharField(label=_("Email or username"), error_messages={'required': _("Either your email or username.")})
    password = forms.CharField(label=_("Password"))

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'usersignin'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        identification = self.cleaned_data.get('identification')
        password = self.cleaned_data.get('password')

        if identification and password:
            user = authenticate(identification=identification, password=password)
            if user is None:
                raise forms.ValidationError(_("Please enter a correct username or email and password. Note that both fields are case-sensitive."))
        return self.cleaned_data
