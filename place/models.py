from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    openTime = models.IntegerField()
    closeTime = models.IntegerField()
    hompage = models.URLField()
    review = models.FloatField()
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name