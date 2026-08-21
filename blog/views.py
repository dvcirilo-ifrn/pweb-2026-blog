from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Mensagem
from .forms import MensagemForm, PostForm

def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/index.html", context)

def posts(request, id_post):
    context = {
        "post": get_object_or_404(Post, id=id_post),
    }
    return render(request, "blog/post.html", context)

def novo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "blog/form_post.html", context)

def editar_post(request, id_post):
    post = get_object_or_404(Post, id=id_post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "is_editar": True,
    }
    return render(request, "blog/form_post.html", context)

def remover_post(request, id_post):
    if request.method == "POST":
        post = get_object_or_404(Post, id=id_post)
        post.delete()
        return redirect("index")
    else:
        return render(request, "blog/confirmar_remocao.html")

def contato(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "blog/contato_resposta.html")
    else:
        form = MensagemForm()
    context = {
        "form": form,
    } 
    return render(request, "blog/contato.html", context)