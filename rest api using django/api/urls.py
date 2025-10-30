from django.urls import path
from api.views import BlogPostListCreateView

urlpatterns = [
    # Define your API endpoints here
    path('api/', BlogPostListCreateView.as_view(), name='Create BlogPosts'),
]