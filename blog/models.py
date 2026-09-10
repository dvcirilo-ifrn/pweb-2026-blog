from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Blog(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    sobre = models.TextField()
    contatos = HTMLField()

    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="posts")
    data = models.DateField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = HTMLField()

    def __str__(self):
        return self.titulo

class Mensagem(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.email