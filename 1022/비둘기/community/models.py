from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=100)
    movie_title=models.CharField(max_length=50)
    rank=models.IntegerField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user_id=models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content=models.CharField(max_length=100)
    review_id=models.IntegerField()
    user_id=models.IntegerField()
    
    def __str__(self):
        return self.title
class Like(models.Model):
    review_id=models.IntegerField()
    user_id=models.IntegerField()
    
    def __str__(self):
        return self.title