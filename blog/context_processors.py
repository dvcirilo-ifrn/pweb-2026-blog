from .models import Blog

def blog_context(request):
    return {
        'blog': Blog.objects.first()
    }