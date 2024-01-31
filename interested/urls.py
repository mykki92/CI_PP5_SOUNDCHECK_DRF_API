from django.urls import path
from interested import views


urlpatterns = [
    path('interested/', views.InterestedListView.as_view()),
    path('interested/<int:pk>/', views.InterestedDetailView.as_view()),
]