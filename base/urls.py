from django.urls import path

from base import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:shorten_link>', views.go, name='go')
]
