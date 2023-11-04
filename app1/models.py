from django.db import models


class User(models.Model):
    Name=models.CharField(max_length=30)
    Mobile=models.IntegerField()
    Email=models.EmailField()
    Amount=models.IntegerField()
