from django.urls import path
from . import views

app_name ="barang"
urlpatterns = [
    path('', views.index, name='index'),
]
