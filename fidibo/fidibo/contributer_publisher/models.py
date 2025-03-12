from django.db import models
from books_magazines.models import Ebooks, Audiobook, Magazines

class Contributers(models.Model):
    name = models.CharField(max_length = 100)
    ebooks = models.ForeignKey(to = Ebooks, on_delete=models.CASCADE, related_name = "ebooks_of_the_author")
    audiobooks = models.ForeignKey(to = Audiobook, on_delete=models.CASCADE, related_name = "audiobooks_of_the_author")
    biography = models.TextField()

class Publishers(models.Model):
    name = models.CharField(max_length = 100)
    ebooks = models.ForeignKey(to = Ebooks, on_delete=models.CASCADE, related_name = "ebooks_of_the_publisher")
    audiobooks = models.ForeignKey(to = Audiobook, on_delete=models.CASCADE, related_name = "audiobooks_of_the_publisher")
    Magazines = models.ForeignKey(to = Magazines, on_delete=models.CASCADE, related_name = "magazines_of_the_publisher")
    biography = models.TextField()