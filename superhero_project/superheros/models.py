from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ablity = models.CharField(max_length=50)
    secondary_ablity = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)

    def _str_(self):
        return self.name