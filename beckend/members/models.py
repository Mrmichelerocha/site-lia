from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

def get_img_upload_path(instance, filename):
    return f'{instance.created_at}/memberspreview/{filename}'

class CategoriaMenbers(models.Model): 
    category = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.category
    
class Achievements(models.Model): 
    achievementsimg = models.ImageField(upload_to=get_img_upload_path)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name

class Members(models.Model):
    imagem = models.ImageField(upload_to=get_img_upload_path)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=300)
    number = models.IntegerField(max_length=200)
    curriculum = models.URLField()
    description = models.TextField()
    achive = models.ForeignKey(Achievements, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoriaMenbers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name