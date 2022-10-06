from django.db import models


class Country(models.Model):
    country = models.CharField(
        "Country", max_length=255, null=True, blank=False)
    code = models.CharField("Code", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField("State", max_length=255, null=True, blank=False)
    code = models.CharField("Code", max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.state


class Language(models.Model):
    Lan = models.CharField("Language", max_length=255, null=True, blank=False)

    def __str__(self):
        return self.Lan

# Create your models here.
