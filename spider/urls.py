from django.urls import path

from . import views

urlpatterns = [
    path('', views.func, name = 'func'),
    path('list/', views.listing, name = 'list'),
    path('search/', views.searching, name = 'search'),
]

