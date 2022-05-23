from django.contrib import admin
from .models import Alumno


# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','correo','direccion','foto_alumno')

admin.site.register(Alumno,AlumnoAdmin)
