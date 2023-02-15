from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('ping/', views.HealthProbeView.as_view()),
    path('',      include('django_prometheus.urls')),
]
