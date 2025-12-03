from django.urls import path

from .views import (
    MutabaahCreateView,
    MutabaahDetailView,
    MutabaahListView,
    MutabaahPDFView,
    MutabaahUpdateView,
)

urlpatterns = [
    path('', MutabaahListView.as_view(), name='mutabaah_list'),
    path('add/', MutabaahCreateView.as_view(), name='mutabaah_add'),
    path('<int:pk>/', MutabaahDetailView.as_view(), name='mutabaah_detail'),
    path('<int:pk>/edit/', MutabaahUpdateView.as_view(), name='mutabaah_edit'),
    path('<int:pk>/pdf/', MutabaahPDFView.as_view(), name='mutabaah_pdf'),
]
