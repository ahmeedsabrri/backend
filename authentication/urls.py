from .views import AddUserView
from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', AddUserView.as_view(), name='register'),
    path('callback/', views.OAuth2CallbackView.as_view(), name='oauth2_callback'),
]