from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
urlpatterns=[
    # path('',views.home,name="blog-home"),   #here why i give name as blog-home because there is a possibility for having another app having same name home ..so it is collapsed so i prefer 'blog-home',then 'home'.
    path('', PostListView.as_view(),name='blog-home'),    #.as_view is given for viewsing class views
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'), 
    path('post/new/', PostCreateView.as_view(),name='post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'), 
    path('about',views.about,name="blog-about"),
]