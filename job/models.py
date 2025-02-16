from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=500)
    pub_date=models.DateField()
    body = models.TextField()
    job_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


