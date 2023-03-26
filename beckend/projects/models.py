from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

def get_img_upload_path(instance, filename):
    return f'{instance.created_at}/projectspreview/{filename}'

class CategoriaProjects(models.Model): 
    category = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.category

class Project(models.Model):
    imagem = models.ImageField(upload_to=get_img_upload_path)
    title = models.CharField(max_length=255)
    description = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(CategoriaProjects, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    