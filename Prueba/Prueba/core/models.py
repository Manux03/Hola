from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password = None):
        if not email:
            raise ValueError ('El Usuario debe contar con un correo electronico')

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres, 
            apellidos = apellidos
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser (self,email,username,nombres,apellidos,password):
        usuario = self.create_user(
            email = email,    
            username = username, 
            nombres = nombres, 
            apellidos = apellidos,
            password = password
        ) 
        usuario.usuario_administrador = True
        usuario.usuario_superuser = True
        usuario.save()
        return usuario

class Tipoitems (models.Model):
    iditems = models.AutoField(primary_key= True, verbose_name ='iditems')
    tipoitems = models.CharField (max_length= 50,verbose_name='Tipoitems')
    def __str__ (self):
        return self.tipoitems

class items (models.Model):
    iditems = models.AutoField(primary_key= True, verbose_name ='iditems')
    nombreitems = models.CharField (max_length= 150,verbose_name='nombreitems')
    descripcionitems = models.CharField (max_length= 250,verbose_name='descripcionitems')
    subir_imagen = models.ImageField(upload_to="imagenes", null= True)
    tipoitems = models.ForeignKey(Tipoitems,on_delete = models.CASCADE, default = 1)
    def __str__ (self):
        return self.nombreitems     



class Usuario (AbstractBaseUser):
    username = models.CharField('Nombre Usuario',unique = 'True', max_length=100)
    email = models.EmailField('Correo Electronico',unique = 'True', max_length=254)
    nombres = models.CharField('Nombre', max_length=200, null = 'False')
    apellidos = models.CharField('Apellido', max_length=200, null = 'False')
    usuario_administrador = models.BooleanField( default = False)
    usuario_superuser = models.BooleanField( default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos'] 

    def _str_(self):
        return f'Usuario {self.username},{self.nombres},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms (self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador

    @property
    def is_superuser(self):
        return self.usuario_superuser