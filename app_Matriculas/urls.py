__author__ = 'user'

from rest_framework import routers
from .viewset import *

#generar las vistas
router = routers.SimpleRouter()
router.register('',AlumnoViewset)
router.register('api/v1.0/matriculas',MatriculaViewset)

urlpatterns = router.urls

