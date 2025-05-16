from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    phone = PhoneNumberField(blank=False, null=False, region="US")
    email = models.EmailField(blank=True, null=True)
    guests = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)

    class Meta:
        ordering = ['date', 'time']
    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"