from django.db import models


class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.PositiveIntegerField()
    email=models.EmailField(max_length=100)
    web=models.URLField(max_length=244)
    age=models.PositiveSmallIntegerField()