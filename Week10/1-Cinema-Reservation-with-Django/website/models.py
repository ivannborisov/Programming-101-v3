from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=120)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Projection(models.Model):
    movie_id = models.ForeignKey(Movie)
    proj_type = models.CharField(max_length=120)
    proj_date = models.DateField()
    proj_time = models.CharField(max_length=60)

    def __str__(self):
        return self.proj_type


class Reservation(models.Model):
    username = models.CharField(max_length=30)
    projections = models.ManyToManyField(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.username
