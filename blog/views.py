from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Mensagem, Blog
from .forms import MensagemForm, PostForm, UserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)  # Separa em páginas de 6 posts
    numero_da_pagina = request.GET.get('pagina')  # Pega o número da página da URL
    print(numero_da_pagina)
    numero_da_pagina = numero_da_pagina if numero_da_pagina else 1
    posts_paginados = paginator.get_page(numero_da_pagina)
    range_elided = paginator.get_elided_page_range(numero_da_pagina, on_each_side=1, on_ends=1)

    context = {
        "posts": posts_paginados,
        "range_elided": range_elided,
        "titulo_blog": Blog.objects.first().titulo
    }
    return render(request, "blog/index.html", context)

def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "registration/cadastro.html", context)

@login_required
@permission_required("blog.view_post")
def posts(request, id_post):
    context = {
        "post": get_object_or_404(Post, id=id_post),
    }
    return render(request, "blog/post.html", context)

@login_required
@permission_required("blog.add_post")
def novo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Postagem criada com sucesso!')
            return redirect("index")
    else:
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "blog/form_post.html", context)

@login_required
@permission_required("blog.change_post")
def editar_post(request, id_post):
    post = get_object_or_404(Post, id=id_post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Postagem editada com sucesso!')
            return redirect("index")
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "is_editar": True,
    }
    return render(request, "blog/form_post.html", context)

@login_required
@permission_required("blog.delete_post")
def remover_post(request, id_post):
    if request.method == "POST":
        post = get_object_or_404(Post, id=id_post)
        post.delete()
        messages.success(request, 'Postagem removida com sucesso!')
        return redirect("index")
    else:
        return render(request, "blog/confirmar_remocao.html")

@login_required
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