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
    #comments=(for when I implement comments)

    def __str__(self):
        return self.title