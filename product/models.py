from django.utils import timezone
from django.db import models
from django.utils.text import slugify



class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    

    def __str__(self):
        return self.name
    


class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    


# class Book(models.Model):
#     name = models.CharField(max_length=250)
#     pages = models.SmallIntegerField()
#     author = models.ForeignKey('Author', on_delete=models.CASCADE)
#     genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True)

    
#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=255, unique=True, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.title)
            super().save(*args, **kwargs)
        