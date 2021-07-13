
from django.urls import path
from django.contrib import admin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import Login,Inicio,logoutUsuario,RegistrarUsuario, lista, eliminar, modifica, agregarcategoriaitem, imagenp, Modificaimagen, Agregarimagen, eliminarimagen
urlpatterns = [
    path('',login_required(Inicio.as_view()), name = 'index'),
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registro'),
    path('lista/',lista,name = 'lista'),
    path('delete/<int:id>/', eliminar,name='employee_delete'),
    path('<int:id>/', modifica,name='employee_update'),
    path('crudimagen/', imagenp,name='imagenp'),
    path('imagen/<int:id>/', Modificaimagen,name='editar_imagen'),
    path('AgregarImagen/', Agregarimagen,name='agregar_imagen'),
    path('eliminar/<int:id>/', eliminarimagen,name='borrar')
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  