from django.urls import path
from . import views

urlpatterns = [
    path('blogFeature/', views.blogFeature),
    path('blog/', views.blogHome),
    path('post/<int:post_id>', views.blogPost),
]