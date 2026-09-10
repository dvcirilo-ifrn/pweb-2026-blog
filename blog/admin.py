from django.contrib import admin
from .models import Post, Mensagem, Blog, User

admin.site.register(Post)
admin.site.register(Mensagem)
admin.site.register(Blog)
admin.site.register(User)
