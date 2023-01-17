from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True)
    content=models.TextField()
    image=models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title