from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class AboutMe(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField()
    my_photo = models.ImageField(blank=True, null=True)
    fb_link = models.CharField(blank=True, null = True, max_length = 250)
    li_link = models.CharField(blank = True, null = True, max_length = 250)
    t_link = models.CharField(blank=True, null = True, max_length = 250)

    def __str__(self):
        return str(self.id)


class MyProject(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField(max_length=250)
    image = models.ImageField(blank=True, null = True)
    technology = models.CharField(max_length = 250)

    def __str__(self):
        return self.title 
        
    def img(self):
        try:
            image = self.image.url 
        except:
            image = ''
        return image
        