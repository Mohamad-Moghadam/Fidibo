from django.db import models
from books_magazines.models import Ebooks

class Contributers(models.Model):
    name = models.CharField(max_length = 100)
    books = models.ForeignKey(to = Ebooks, on_delete=models.CASCADE, related_name = "books_of_the_author")
    biography = models.TextField()

class Publishers(models.Model):
    name = models.CharField(max_length = 100)
    books = models.ForeignKey(to = Ebooks, on_delete=models.CASCADE, related_name = "books_of_the_author")
    biography = models.TextField()