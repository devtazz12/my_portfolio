from django.db import models

# Create your models here.

class ContactMe(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.fname
    
