from django.urls import path, include
from .views import MyTemplView
from django.views.generic import TemplateView

urlpatterns = [
    path('', MyTemplView.as_view(), name='landing'),
]