from typing import Any
from django.db import models

# Create your models here.
class Blockpost(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return(self.title)