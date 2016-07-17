from django.views.generic import (TemplateView, CreateView)
from hack.models import Hack
from hack.forms import HackForm


class HomeView(TemplateView):
    template_name = "hack/home.html"


class NewHackView(CreateView):
    model = Hack
    form_class = HackForm
    template_name = "hack/newHack.html"
