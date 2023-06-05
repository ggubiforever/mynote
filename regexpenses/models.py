from django.db import models


class expenses(models.Model):
    cat = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    amt = models.CharField(max_length=10)
    amtdate = models.DateTimeField()
    monthly_avr = models.CharField(max_length=10)

class daily_target(models.Model):
    target = models.CharField(max_length=20)
