from django.conf.urls import url
from accounts.views import SignUpView, SignInView

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name="user_signup"),
    url(r'^signin/$', SignInView.as_view(), name="user_signin"),
]
