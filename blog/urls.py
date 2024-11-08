from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # run the PostListView when we hit "/"
    path('', PostListView.as_view(), name='blog-home'),
    # run the PostListView when we hit "/"
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # run the PostListView when we hit "/post/1/"
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # run the PostCreateView when we hit "/post/new/"
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # run the PostUpdateView when we hit "/post/1/update"
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # run the PostDeleteView when we hit "/post/1/"
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # run about view function when we hit "about/"
    path('about/', views.about, name='blog-about'),
]
