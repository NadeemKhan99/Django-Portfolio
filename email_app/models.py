from django.db import models

# Create your models here.

class EmailSender(models.Model):

    email = models.EmailField()
    description = models.TextField()
