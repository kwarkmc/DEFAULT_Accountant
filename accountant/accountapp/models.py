from django.db import models
from django.utils import timezone

# Create your models here.

class Accountant(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()
    price = models.IntegerField(default=0, null=True)
    
def __str__(self):
    return self.title
