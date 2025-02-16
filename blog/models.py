from django.db import models


class Blog(models.Model):
    image= models.ImageField(upload_to='images/')
    full_summary = models.CharField(max_length=5200)

