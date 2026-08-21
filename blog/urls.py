from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:id_post>/", views.posts, name="posts"),
    path("posts/<int:id_post>/remover", views.remover_post, name="remover_post"),
    path("posts/<int:id_post>/editar", views.editar_post, name="editar_post"),
    path("posts/novo/", views.novo_post, name="novo_post"),
    path("contato/", views.contato, name="contato"),
]