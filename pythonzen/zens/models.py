from django.db import models

class Quote(models.Model):
    text = models.CharField(max_length=128)

