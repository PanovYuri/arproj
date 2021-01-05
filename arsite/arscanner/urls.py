from django.urls import path

from . import views

app_name = 'arscanner'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:ar_uuid>/', views.details, name="details"),
    path('<uuid:ar_uuid>/scann', views.scanning, name="scanning"),
    path('append', views.append_card, name="appendcard")
]