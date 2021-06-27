"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('estudiante/<int:id>', views.obtener_edificio, 
            name='obtener_edificio'),
        path('crear/estudiante', views.crear_edificio, 
            name='crear_edificio'),
        path('editar_estudiante/<int:id>', views.editar_edificio, 
            name='editar_edificio'),
        path('eliminar/estudiante/<int:id>', views.eliminar_edificio, 
            name='eliminar_edificio'),
        # numeros telefonicos
        path('crear/numero/telefonico', views.crear_Departamento, 
            name='crear_Departamento'),
        path('editar/numero/telefonico/<int:id>', views.editar_Departamentoo, 
            name='editar_Departamentoo'),
        path('crear/numero/telefonico/estudiante/<int:id>', views.crear_numero_Departamento, 
            name='crear_numero_Departamento'),
        
 ]
