from django.db import models

# Create your models here.
class viagem(models.Model):
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()

    def __str__(self):
        return f"{self.destino} ({self.data_ida} a {self.data_volta})"