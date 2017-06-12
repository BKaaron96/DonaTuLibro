from django.db import models

# Create your models here.
class Login(models.Model):
    usuario=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=20)

class Registro(models.Model):
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   telefono = models.CharField(max_length=15)
   dni=models.CharField(max_length=9)
   correo = models.EmailField(max_length=254)
   usuario = models.CharField(max_length=20)
   contraseña1 = models.CharField(max_length=20)
   contraseña2 = models.CharField(max_length=20)
   tipodeusuario = models.CharField(max_length=20)
   colegio = models.CharField(max_length=20)
