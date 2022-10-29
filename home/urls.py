from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name="homepage"),
    path('add/', Add, name="adduser"),
    path('delete/<int:id>', Delete, name="delete"),
    path('update/<int:id>', Update, name="update"),
]