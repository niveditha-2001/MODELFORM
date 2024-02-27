from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    mob=models.IntegerField()
