from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Letter
from wargas.models import Warga

# Create your views here.
# class LetterListView(ListView):
#     model = Article
#     template_name = 'article_list.html'
#
#

#
#
# class LetterUpdateView(UpdateView):
#     model = Article
#     fields = ('title', 'foto', 'body',)
#     template_name = 'article_edit.html'
#
#
# class LetterDeleteView(DeleteView):
#     model = Article
#     template_name = 'article_delete.html'
#     success_url = reverse_lazy('article_list')
#

class LetterCreateView(CreateView):
    model = Letter
    template_name = 'surat_new.html'
    fields = ("biodata" , "tujuan", "perihal", "author")


class LetterDetailView(DetailView):
    model = Letter
    template_name = 'surat_pengantar.html'



