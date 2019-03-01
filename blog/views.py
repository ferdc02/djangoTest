from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'Feron',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_psted': 'Agosto 23, 2018'
    },
    {
        'author': 'Troy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_psted': 'Agosto 29, 2018'



    
    }

]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
