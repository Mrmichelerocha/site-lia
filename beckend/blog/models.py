from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

def get_img_upload_path(instance, filename):
    return f'{instance.created_at}/blogpreview/{filename}'

class Blog(models.Model):
    imagem = models.ImageField(upload_to=get_img_upload_path)
    title = models.CharField(max_length=255)
    description = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title