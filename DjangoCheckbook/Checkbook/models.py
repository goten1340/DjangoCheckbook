from django.db import models
from django.db.models import Model, FloatField

# Create your models here.

Transaction_Choices = (
    ("Deposit", "Deposit"),
    ("Withdraw", "Withdraw"),)


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=1000, decimal_places=2)

    Accounts = models.Manager()

    # Allows references to a specific account be returned
    # as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Transaction(models.Model):
    date_Of_Transaction = models.DateField()
    type_Of_Transaction = models.CharField(choices=Transaction_Choices, max_length=10)
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transaction = models.Manager()
