from django.urls import path
from . import views

urlpatterns = [
    path('projectFeature/', views.projectFeature),
    path('project/', views.projectHome),
    path('project/<int:post_id>', views.projectPost),
]