from django.urls import path
from . import views

app_name = 'inventary'

urlpatterns = [
    path('', views.index, name="index")
]