from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model): # Se va a crear una clase HEREDADA de models.Model que viene integrada en Django
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Función para que al meter el nombre de la clase devuelva lo que se le pide aquí en vez
        de valores extraños'''
        return self.user.username