from django.urls import path

from . import views

app_name = 'regexpenses'

urlpatterns = [
    path('', views.index, name='index'),
]