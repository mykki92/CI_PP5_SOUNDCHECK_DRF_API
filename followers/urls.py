from django.urls import path
from likes import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
]