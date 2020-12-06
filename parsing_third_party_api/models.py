from django.db import models


# Create your models here.
class CurrencyModel(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    charCode = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return "%s,%s,%s, %s,%s, %s," % (self.day, self.month, self.year, self.charCode, self.name, self.value)
