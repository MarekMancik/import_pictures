from django.db import models

# Create your models here.


# my_model = models.Model
class MojeTabulka(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    post_code = models.IntegerField()


class DalsiTabulka(models.Model):
    pet = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
