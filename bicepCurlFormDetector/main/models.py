from django.db import models

# Create your models here.


class Person(models.Model):
    HAND_OPTIONS = [
        ("Lt", "Left"),
        ("Rt", "Right"),
        ("Null", "Select"),
    ]
    hand = models.CharField(max_length=7, choices=HAND_OPTIONS)
