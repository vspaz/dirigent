from django.urls import path

from .views.service import health

urlpatterns = [
    path('ping/', health.PingView.as_view()),
]