from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.SearchView.as_view(), name='home'),
]
