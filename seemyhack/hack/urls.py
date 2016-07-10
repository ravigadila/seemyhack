from django.conf.urls import url
from hack.views import HomeView

urlpatterns = [
    url(r'^', HomeView.as_view(), name="home")
]
