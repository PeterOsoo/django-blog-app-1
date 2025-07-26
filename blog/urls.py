from django.urls import path
from .views import BlogPostListView, CreateBlogPostView, create_post_view, blog_list_view


urlpatterns = [
    path('', blog_list_view, name='blog-posts'),  # 👉 now serves HTML
    path('create/', create_post_view, name='create-post'),
    path('api/create/', CreateBlogPostView.as_view(), name='api-create-post'),
    path('api/posts/', BlogPostListView.as_view(), name='api-posts'),  # 👉 moved here
]
