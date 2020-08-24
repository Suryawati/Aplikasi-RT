from django.urls import path

from .views import (
    KasListView,

)

urlpatterns = [

    path('', KasListView.as_view(), name='kas'),
]
