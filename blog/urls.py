from django.urls import path
from .views import BlogListView, BlogDetailVew

urlpatterns = [
    path('post/<int:pk>/', BlogDetailVew.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]