from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles),
    path('blog/', views.blogHome),
    path('post/<int:post_id>', views.blogPost),
]