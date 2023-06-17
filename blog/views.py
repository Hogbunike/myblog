from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'Henry',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'June 13 2023',
#     },
#     {
#         'author': 'Fred',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'June 14 2023',
#     },
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'Aboutpage'})