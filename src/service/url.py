from django.urls import include, path

from . import views

urlpatterns = [
    path('ping/', views.HealthProbeView.as_view()),
    path('',      include('django_prometheus.urls')),
]
