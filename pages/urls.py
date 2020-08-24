from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dashboard/', views.DashPageView.as_view(), name='dashboard'),
    path('userprofile/', views.UserPageView.as_view(), name='user_profile'),
]
