from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from accounts.forms import SignupForm, SignInForm


class SignUpView(FormView):
    """
    Allow user to create new account in this site
    """
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('hack:home')

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)


class SignInView(FormView):
    """
    Allow user to sign in to their own accounts
    """
    form_class = SignInForm
    template_name = "accounts/signin.html"
    success_url = reverse_lazy('hack:home')

    def form_valid(self, form):
        identification, password = (form.cleaned_data['identification'],
                                    form.cleaned_data['password'])
        user = authenticate(email=identification,
                            password=password)
        if user.is_active:
            login(self.request, user)
        else:
            return redirect(reverse('hack:home'))
        return super(SignInView, self).form_valid(form)


class SignOutView(View):
    """
    Sign Out from account
    """
    def get(self, request):
        logout(request)
        return redirect(reverse('hack:home'))
