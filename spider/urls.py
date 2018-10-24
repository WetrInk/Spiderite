from django.urls import path

from . import views

urlpatterns = [
    path('', views.func, name = 'func'),
    path('list/', views.listing, name = 'list'),
    path('search/', views.searching, name = 'search'),
    path('1/', views.ContentSearch, name = 'Content Search'),
    path('2/', views.TimeSearch, name = "Time Search"),
]
