from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from social_django.utils import load_backend, load_strategy

class GoogleLoginAPIView(APIView):
    def get(self, request):
        strategy = load_strategy(request)
        backend = load_backend(strategy, 'google-oauth2', redirect_uri=None)
        auth_url = backend.auth_url()
        return redirect(auth_url)

class GoogleAuthCallbackView(View):
    def get(self, request):
        code = request.GET.get('code')
        strategy = load_strategy(request)
        backend = load_backend(strategy, 'google-oauth2', redirect_uri=None)
        user = backend.auth_complete(request, {'code': code})
        login(request, user)
        # Trả về token cho ứng dụng Flutter
        return JsonResponse({'token': 'your-token'})
