from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)

class Denuncia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='denuncias')
    tipo_denuncia = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='denuncias/')
    descricao = models.TextField()
    local_denuncia = models.CharField(max_length=500)

    def __str__(self):
        return f'Denúncia de {self.user.username} - {self.tipo_denuncia}'
