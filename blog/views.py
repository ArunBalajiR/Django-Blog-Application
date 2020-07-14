from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # posts=[
    #     {
    #         'author': 'Arun Balaji',
    #         'title': 'Django Tutorials',
    #         'content': 'First Post Content',
    #         'date_posted': '15th Jan 2020'
    #     },
    #     {
    #         'author': 'Vijaya Baskar',
    #         'title': 'Python Tutorials',
    #         'content': 'Second Post Content',
    #         'date_posted': '25th Jun 2020'
    #     }
    # ]
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})