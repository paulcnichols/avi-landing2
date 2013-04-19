from django.db import models

# Create your models here.
class Interested(models.Model):
    email = models.EmailField()
    when = models.DateField(auto_now_add=True)
