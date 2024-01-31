from django.urls import path

from . import views


urlpatterns = [
    path('attending/', views.AttendingListView.as_view()),
    path('attending/<int:pk>/', views.AttendingDetailView.as_view()),
]