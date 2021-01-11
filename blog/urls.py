from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,

    ProjectListView,ProjectDetailView,
   )
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'), 
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('detail/<int:post_id>/', views.post_detail, name='post-detail'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    #---------------------------------------project model 
    path('project/', ProjectListView.as_view(), name='project-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/',views.allProjects,name='allPosts'),


      path('about/', views.about, name='blog-about'),
        path('training/', views.training, name='blog-training'),
]