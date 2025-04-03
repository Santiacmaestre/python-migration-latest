from django.urls import path
from django.http import JsonResponse
from app.admin import custom_admin_site

def greet_api(request):
    return JsonResponse({"message": "Hello from Django + React"})

urlpatterns = [
    path("admin/", custom_admin_site.urls),
    path("api/greet/", greet_api),
]
