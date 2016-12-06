from django.shortcuts import render
from blog.posts.models import Post

# Create your views here.

def home(request):
	posts = Post.objects.all()
	return render(request, 'core/index.html', {'posts': posts})
