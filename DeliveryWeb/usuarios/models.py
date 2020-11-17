from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class local(models.Model):

    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    clave = models.CharField(max_length=200)
    confirmarClave = models.CharField(max_length=200)

    tipo = (
        ('1', 'Gastronomica'),
        ('2', 'Salud'),
        ('3', 'Logistica'),

    )


    tipoEmpresa= models.CharField(
        max_length=1,
        choices= tipo,
        blank = True,
        default = 0,
        help_text= 'Tipo de empresa',
    )

    class meta:
        ordering = ['nombre', 'direccion']
    
    def get_absolute_url(self):
        return reverse('local_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.nombre}, {self.direccion}'
    
    


