from django.db import models


# Create your models here.
class short_link(models.Model):
    link = models.CharField(max_length=1000)
    shorten_link = models.CharField(max_length=100)

    def __str__(self):
        return str(self.link)
