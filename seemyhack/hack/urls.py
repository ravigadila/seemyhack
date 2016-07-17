from django.conf.urls import url
from hack.views import HomeView, NewHackView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^add-new-hack/$', NewHackView.as_view(), name="add_new_hack")
]
