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

tipo_matricula = [
    ('ORDINARIA','ORDINARIA'),
    ('EXTRAORDINARIA','EXTRAORDINARIA'),
    ('ESPECIAL','ESPACIAL'),
]

tipo_curso = [
    ('I','I CICLO'),
    ('II','II CICLO'),
    ('III','III CICLO'),
    ('IV','IV CICLO'),
    ('V','V CICLO'),
]

class Matricula(models.Model):

    codigo = models.CharField(max_length=8, blank=False)
    tipo = models.CharField(max_length=45, choices=tipo_matricula, default='available')
    fecha = models.DateField(blank=False)
    curso = models.CharField(max_length=45, choices=tipo_curso, default='available')
    carrera = models.CharField(max_length=100, blank=False)
    fk_alumno = models.OneToOneField(Alumno,on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.tipo



