from django.db import models
from django.utils import timezone


class Account(models.Model):
    id = models.UUIDField(primary_key=True)
    type = models.IntegerField()
    bank = models.CharField(max_length=20)
    number = models.IntegerField()
    balance = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(blank=True, null=True)

    def open(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.bank + ' ' + self.number


class AccountTransfer(models.Model):
    id = models.UUIDField(primary_key=True)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='from_account')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_account')
    automatic_flag = models.IntegerField()
    amount = models.IntegerField()
    start_date = models.DateTimeField()
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.from_account_id + ' -> ' + self.to_account_id


class Product(models.Model):
    id = models.UUIDField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=20)
    maturity_amount = models.IntegerField()
    interest_rate = models.FloatField()
    payment_amount = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(blank=True, null=True)
