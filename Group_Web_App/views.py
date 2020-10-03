from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPage(LoginRequiredMixin,TemplateView):
    template_name = 'main.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

