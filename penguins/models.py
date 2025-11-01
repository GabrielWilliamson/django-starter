from django.db import models

class Penguin(models.Model):
    name=models.CharField("Name")
    age=models.IntegerField("Age")

    class Meta:
        verbose_name = "Penguin"
        verbose_name_plural = "Penguins"
