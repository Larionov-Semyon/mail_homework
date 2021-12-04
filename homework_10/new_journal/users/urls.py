from django.urls import path
from .views import verify

urlpatterns = [
    path('verify/<uuid:uuid>/', verify, name='verify'),
]
