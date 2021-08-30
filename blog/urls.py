# blog/urls.py
# http://127.0.0.1:8000/blog/ 블로그 리스트 페이지로 이동
# http://127.0.0.1:8000/blog/1 1번 글 상세보기 페이지로 이동
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.detail, name='detail'),
]