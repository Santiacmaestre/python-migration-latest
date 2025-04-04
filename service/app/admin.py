from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.http import HttpResponse
import django
import sys
import django

class CustomAdminSite(admin.AdminSite):
    site_header = "ELITEA Admin"
    site_title = "ELITEA Dashboard"
    index_title = "Welcome to ELITEA Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('version-info/', self.admin_view(self.version_info_view)),
        ]
        return custom_urls + urls

    def index(self, request, extra_context=None):
        python_version = sys.version.split(" ")[0]
        django_version = django.get_version()
        extra_context = extra_context or {}
        extra_context['version_info'] = f"Python {python_version} • Django {django_version}"
        return super().index(request, extra_context=extra_context)

    def version_info_view(self, request):
        python_version = sys.version
        django_version = django.get_version()
        return HttpResponse(f"<h2>Python: {python_version}</h2><h2>Django: {django_version}</h2>")
    
    def login(self, request, extra_context=None):
        import sys
import django
        import django

        extra_context = extra_context or {}
        extra_context["python_version"] = sys.version.split(" ")[0]
        extra_context["django_version"] = django.get_version()

        return super().login(request, extra_context=extra_context)

# Register custom admin
custom_admin_site = CustomAdminSite(name='custom_admin')
