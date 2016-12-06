from blog.posts.models import Categoria

def lista_categorias(request):
    return {
        'lista_categorias': Categoria.objects.all()
    }
