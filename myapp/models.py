from django.db import models

class customModel(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}"
