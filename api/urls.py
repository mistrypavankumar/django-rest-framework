from django.urls import path, include
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroyView.as_view(), name='update-destroy-blogpost'),
    path('custom-blogposts/', views.CustomBlogPostView.as_view(), name='custom-blogpost-view'),
]