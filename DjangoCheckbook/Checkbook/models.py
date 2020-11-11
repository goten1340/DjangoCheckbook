from django.db import models
from django.db.models import Model, FloatField

# Create your models here.

Transaction_Choices = (
    ("Deposit", "Deposit"),
    ("Withdraw", "Withdraw"),)


class Account(models.Model):
    first_name = models.CharField(max_length=50, default='first name')
    last_name = models.CharField(max_length=50, default='last name2')
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    Accounts = models.Manager()

    # Allows references to a specific account be returned
    # as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Transaction(models.Model):
    date_Of_Transaction = models.DateField(default='2/14/1997')
    type_Of_Transaction = models.CharField(choices=Transaction_Choices, max_length=10)
    amount = models.FloatField(default=0.00)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transaction = models.Manager()
