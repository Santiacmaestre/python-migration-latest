from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def greet_api(request):
    return JsonResponse({"message": "Hello from Django + React"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/greet/', greet_api),
]
