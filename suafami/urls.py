from django.urls import path
from .views import GoogleLoginAPIView, GoogleAuthCallbackView

urlpatterns = [
    path('auth/google/', GoogleLoginAPIView.as_view(), name='google-login'),
    path('auth/google/callback/', GoogleAuthCallbackView.as_view(), name='google-callback'),
]
