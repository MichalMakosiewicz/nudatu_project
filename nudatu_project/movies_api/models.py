from django.db import models
import django.db.models.deletion


class Movie(models.Model):
    name = models.CharField(max_length=50)
    total_comments = models.IntegerField()
    rank = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=django.db.models.deletion.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return "[%s] %s" % (self.author, self.text)
