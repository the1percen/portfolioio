from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    text = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name

    
    