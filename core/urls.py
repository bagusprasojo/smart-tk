from django.urls import path

from .views import DashboardView, LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
