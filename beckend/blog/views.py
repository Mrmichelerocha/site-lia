from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blogFeature(request):
  dados = Blog.objects.all()
  return render(request, 'BlogFeature.html', {'dados': dados})

def blogHome(request):
  posts = {}
  posts['post'] = Blog.objects.all()
  return render(request, 'home/BlogHome.html', posts)

def blogPost(request, post_id):
  post = {}
  post['post'] = Blog.objects.get(pk=post_id)
  return render(request, 'post/BlogPost.html', post)