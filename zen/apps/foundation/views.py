# Create your views here.
from django.views.generic import TemplateView


class FoundationTemplateView(TemplateView):
    template_name = 'home.html'
