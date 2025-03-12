from django.db import models
from contributers.models import Contributers

class Ebooks(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "publishers")
    time_to_read = models.DateTimeField()
    date_of_publish = models.DateField()


