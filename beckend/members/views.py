from django.shortcuts import render
from members.models import Members

# Create your views here.
def members(request):
  dados = Members.objects.all()
  return render(request, 'membersCore.html', {'dados': dados})

def MemberPost(request, post_id):
  post = {}
  post['post'] = Members.objects.get(pk=post_id)
  return render(request, 'member/memberPost.html', post)