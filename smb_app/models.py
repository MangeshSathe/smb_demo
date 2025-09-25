from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(max_length=5, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title