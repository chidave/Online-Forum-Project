from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    #author=(for when i have user set up)
    #comments=(for when I implement comments)

    def __str__(self):
        return self.title