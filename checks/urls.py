from django.urls import path
from checks import views

urlpatterns = [
    path('checks/', views.CheckList.as_view()),
    path('checks/<int:pk>/', views.CheckDetail.as_view()),
]
