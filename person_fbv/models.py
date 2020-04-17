from django.db import models
from django.urls import reverse

#This class defines the charactristics of a book. The book has a Name and Pages
#More details in the book can be added by adding variables in this class
class Person(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    #Used for updating details of an individual
    def get_absolute_url(self):
        return reverse('person_fbv:person_edit', kwargs={'pk': self.pk})