from django.db import models

class Ebooks(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE)
    time_to_read = models.DateTimeField()
    date_of_publish = models.DateField()