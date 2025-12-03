from django.urls import path

from .views import StudentCreateView, StudentDetailView, StudentListView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('add/', StudentCreateView.as_view(), name='student_add'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
