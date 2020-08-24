from django.views.generic import ListView

from django.urls import reverse_lazy

from .models import Kas
class KasListView(ListView):
    model = Kas
    template_name = 'kas.html'


