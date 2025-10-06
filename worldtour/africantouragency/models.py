from django.db import models

# Create your models here.


class Tour(models.Model):
    # explicitly define the id field for static analysis tools
    # this is not really needed to define the id but to avoid vscode from throwing errors
    id = models.AutoField(primary_key=True)

    # set origin country, destination, number of nights and price for the tour
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # String representation of the tours
    def __str__(self):
        return (f"ID {self.id}:- From: {self.origin_country}, To:{self.destination_country}, No of nights:{self.number_of_nights}, Nights cost: ${self.price}")
