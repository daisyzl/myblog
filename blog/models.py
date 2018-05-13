from django.db import models

from django.db import  models

class Article(models.Model):
    title=models.CharField(max_length=32,default='Title')
    content=models.TextField(null=True)

    def __str__(self):#python3
        return self.title