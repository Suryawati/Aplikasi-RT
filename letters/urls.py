from django.urls import path

from .views import (

    LetterCreateView, # new
    LetterDetailView,
    #LetterListView,
)

urlpatterns = [
    # path('<int:pk>/edit/',
    #       ArticleUpdateView.as_view(), name='surat_edit'),
    path('<int:pk>/',
          LetterDetailView.as_view(), name='surat_pengantar'),
    # path('<int:pk>/delete/',
    #      ArticleDeleteView.as_view(), name='surat_delete'),
    path('new/', LetterCreateView.as_view(), name='surat_new'),
    # path('', ArticleListView.as_view(), name='surat_list'),
]
