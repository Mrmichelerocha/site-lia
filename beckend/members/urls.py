from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members),
    path('member/<int:post_id>', views.MemberPost),
]