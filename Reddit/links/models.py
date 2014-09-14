from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(verify_exists=False,max_length=200)
    positive_votes = models.PositiveIntegerField(default=0)
    negative_votes = models.PositiveIntegerField(default=0)
