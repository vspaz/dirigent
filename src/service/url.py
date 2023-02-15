from django.urls import path

from . import views

urlpatterns = [
    path('ping/', views.HealthProbeView.as_view()),
]
