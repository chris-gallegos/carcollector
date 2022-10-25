from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()


    def __str__(self):
        return self.brand
    

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


class Show(models.Model):
  date = models.DateField('show date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  car = models.ForeignKey(Car, on_delete=models.CASCADE)



  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
