from django.db import models

# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length=255)
    description= models.TextField()
    slug=models.SlugField(max_length=255,unique=True)
    published_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    