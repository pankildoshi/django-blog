from cgitb import text
from email import message
import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=110)
    email = models.CharField(max_length=110)
    subject = models.CharField(max_length=110)
    message = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.subject, self.name)