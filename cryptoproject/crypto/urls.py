from django.urls import path
from . import views

urlpatterns = [
    path('',views.CryptoView,name='all'),
    path('test/',views.index)
]