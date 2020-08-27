from django.db import models
import datetime
import json


class Vehicle(models.Model):
    license_plate_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default='Other')
    is_valid = models.BooleanField(default=True)
    time_stamp = models.TimeField(default=datetime.datetime.now())
