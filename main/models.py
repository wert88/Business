from django.db import models
from django import forms

class Picture(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" +  self.email