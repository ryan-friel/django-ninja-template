from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
    description = models.TextField(max_length=255, null=True, blank=False)
