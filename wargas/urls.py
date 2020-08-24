from django.urls import path
from django.conf.urls import url

from .views import (
    WargaListView,
    WargaDetailView,
    TabelListView,


)

urlpatterns = [
    path('warga/<int:pk>/',
         WargaDetailView.as_view(), name='warga_detail'),
    path('listwarga/', WargaListView.search , name='warga_list'),
    path('tabel/', TabelListView.as_view(), name='warga_table'),
    #url(r'^(?P<no>\d+)', TabelListView, name='warga_table'),

]
