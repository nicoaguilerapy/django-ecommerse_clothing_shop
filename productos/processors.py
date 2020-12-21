from .models import Categoria

def ctx_dict(request):
    ctx = {}
    ctx['categorias'] = Categoria.objects.all()
    return ctx
