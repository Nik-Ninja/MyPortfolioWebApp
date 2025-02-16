from django.shortcuts import render
from .models import Blog


def goToHomePage(request):
    blogs = Blog.objects
    return render(request, 'blog/mainPage.html', {'blogs': blogs})
