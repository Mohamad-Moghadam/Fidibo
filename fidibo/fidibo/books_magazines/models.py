from django.db import models
from contributer_publisher.models import Contributers, Publishers

class Ebooks(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "publishers")
    time_to_read = models.DateTimeField()
    date_of_publish = models.DateField()
    describtion = models.TextField()
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()

class Audiobook(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "publishers")
    date_of_publish = models.DateField()
    narrator = models.CharField(max_length = 50)
    describtion = models.TextField()
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()


class Magazines(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "publishers")
    time_to_read = models.DateTimeField()
    date_of_publish = models.DateField()
    describtion = models.TextField()
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()


class Educational_Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "publishers")
    time_to_read = models.DateTimeField()
    date_of_publish = models.DateField()
    describtion = models.TextField()
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()

