from django.db import models

# Create your models here.
class Classdetail(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    tags = models.TextField(default="")
    blurb = models.TextField(default="")
    def __str__(self):
        return self.name