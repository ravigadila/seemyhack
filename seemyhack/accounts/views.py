from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from accounts.forms import SignupForm, SignInForm


class SignUpView(FormView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('hack:home')

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)


class SignInView(FormView):
    form_class = SignInForm
    template_name = "accounts/signin.html"
    success_url = reverse_lazy('hack:home')

    def form_valid(self, form):
        identification, password = (form.cleaned_data['identification'],
                                    form.cleaned_data['password'])
        user = authenticate(identification=identification,
                            password=password)
        if user.is_active:
            login(self.request, user)
        else:
            return redirect(reverse('hack:home'))
        return super(SignInView, self).form_valid(form)
