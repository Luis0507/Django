from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summry = models.CharField(max_length=200)
    detalle = models.TextField()
    experto = models.BooleanField(null=True)
    desde = models.DateField(null=True)
    hasta = models.DateField(null=True)

    # Los datos que van a mostar en el admin
    def __str__(self):
        return self.detalle

