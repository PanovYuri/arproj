from django.urls import path

from . import views

app_name = 'arscanner'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ar_id>/', views.details, name="details"),
    path('<int:ar_id>/scann', views.scanning, name="scanning"),
]