from django.urls import path
from app11.views import contacto

urlpatterns = [
    path('contacto/', contacto),
]
