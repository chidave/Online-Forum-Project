from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    #comments=models.Man

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True
    )
    content=models.TextField()

    def __str__(self):
        return self.content