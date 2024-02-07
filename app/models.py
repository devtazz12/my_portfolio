from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name
    


class SocialMediaUrl(models.Model):
    name=models.CharField(max_length=30)
    url=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    

class MyCV(models.Model):
    cv=models.FileField(upload_to="file")

    
    
class MyWork(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name
    
      
    
