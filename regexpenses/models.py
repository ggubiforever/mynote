from django.db import models


class expenses(models.Model):
    CHOICES = (
        (0, '기본식비(외식등)'),
        (1, '유흥(놀고먹는거)'),
        (2, '기타'),
    )

    cat = models.IntegerField(default=0, choices=CHOICES)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    amt = models.CharField(max_length=10)
    amtdate = models.DateTimeField()
    monthly_avr = models.CharField(max_length=10)

class daily_target(models.Model):
    target = models.CharField(max_length=20)
