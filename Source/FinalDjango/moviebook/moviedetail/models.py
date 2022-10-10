from distutils.command.upload import upload
from django.db import models


class Language(models.Model):
    name = models.CharField("Language", max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField("ShowName", max_length=100, null=True, blank=False)
    starttime = models.TimeField("Starttime", null=True, blank=False)
    endtime = models.TimeField("EndTime", null=True, blank=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField("MovieName", max_length=100,
                            null=True, blank=False)
    actor = models.CharField(
        "ActorName", max_length=100, null=True, blank=False)
    startdate = models.DateField("StartDate", null=True, blank=False)
    enddate = models.DateField("EndDate", null=True, blank=True)
    show = models.ManyToManyField(Show)
    language = models.ManyToManyField(Language)
    movieimage = models.ImageField(
        upload_to='media/picture/', null=True, blank=False)
    amount = models.FloatField("Amount", null=True, blank=True)

    def __str__(self):
        return self.name
