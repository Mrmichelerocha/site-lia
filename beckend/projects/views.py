from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projectFeature(request):
  dados = Project.objects.all()
  return render(request, 'ProjectsFeature.html', {'dados': dados})

def projectHome(request):
  posts = {}
  posts['post'] = Project.objects.all()
  return render(request, 'home/ProjectsHome.html', posts)

def projectPost(request, post_id):
  post = {}
  post['post'] = Project.objects.get(pk=post_id)
  return render(request, 'post/ProjectPost.html', post)