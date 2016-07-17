from django.conf.urls import url
from accounts.views import SignUpView, SignInView, SignOutView

urlpatterns = [

    # user authentication urls
    url(r'^signup/$', SignUpView.as_view(), name="user_signup"),
    url(r'^signin/$', SignInView.as_view(), name="user_signin"),
    url(r'^signout/$', SignOutView.as_view(), name="user_signout"),
]
