from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index1/',views.index1,name='index1'),
    path('sample1/',views.sample1,name='sample1'),
]
