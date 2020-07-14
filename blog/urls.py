from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="blog-home"),   #here why i give name as blog-home because there is a possibility for having another app having same name home ..so it is collapsed so i prefer 'blog-home',then 'home'.
    path('about',views.about,name="blog-about")
]