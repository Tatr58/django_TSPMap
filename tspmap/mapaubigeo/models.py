from django.db import models

# Create your models here.
class CentroPoblado(models.Model):
    
    codigo = models.CharField(max_length=200)
    nombre_cp = models.CharField(max_length=200)
    distrito = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=9, decimal_places=7)
    longitud = models.DecimalField(max_digits=9, decimal_places=7)

    def __str__(self):
        return 'CP: {0} DS:{1} PR:{2} RG: {3}'.format(self.nombre_cp, self.distrito, self.provincia, self.region)
