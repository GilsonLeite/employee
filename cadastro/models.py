from django.db import models


class Cadastro(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=64)
    active = models.BooleanField()

    def __str__(self):
        return self.name
