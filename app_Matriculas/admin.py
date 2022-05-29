from django.contrib import admin
from .models import Alumno, Matricula


# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','correo','direccion','foto_alumno')

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('codigo','fk_alumno','tipo','fecha','curso','carrera')
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Matricula,MatriculaAdmin)
