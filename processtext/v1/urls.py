from django.urls import path
from .views import *

urlpatterns = [
    path('process_text', process_text_view, name='process_text'),
]