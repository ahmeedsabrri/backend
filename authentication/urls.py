from django.urls import path

from .views import AddUserView

urlpatterns = [
    path('register/', AddUserView.as_view(), name='register'),
]