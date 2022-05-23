from django.db import models
from django.utils.safestring import mark_safe


def url(self,filename):
    ruta = 'static/img/alumnos/%s/%s'%(self.nombre,str(filename))
    return ruta

class Alumno(models.Model):

    def foto_alumno(self):
        return mark_safe('<a href="/%s"> <img src="/%s" width=50px height=50px /> </a>'%(self.foto,self.foto))

    nombre =models.CharField(max_length=45, blank=False)
    apellido =models.CharField(max_length=45, blank=False)
    telefono =models.IntegerField(blank=False)
    correo=models.EmailField(blank=False)
    direccion = models.CharField(max_length=100, blank=False)
    foto=models.ImageField(upload_to=url)



    def __str__(self):
        return self.nombre


