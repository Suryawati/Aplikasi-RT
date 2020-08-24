from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.db.models import Q
from .models import Warga


class WargaCreateView(CreateView):
    model = Warga
    template_name = 'warga_list.html'
    fields = ('biodata','perihal')


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga_detail.html'

class TabelListView(ListView):
    model = Warga
    template_name = 'warga_table.html'

    def get(self, request):
        lists = Warga.objects.all().order_by('no_rumah')
        #print(lists)
        #lists = Warga.objects.filter(nama="Shinta")

        args = { 'lists' : lists}
        return render(request, self.template_name, args)

class WargaListView(ListView):
    model = Warga
    #context_object_name = 'wargas_list'

    a = Warga.objects.filter(nama="Shinta")
    print(a)
    def search(request):
        query = request.GET.get('q', '')
        template_name = 'warga_list.html'
        print(query)
        if query:
            queryset = (Q(noktp=query))
            result = Warga.objects.filter(queryset)
        else:
            result = []

        return render(request, template_name, {'result': result, 'query': query})