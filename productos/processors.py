from .models import Category

def ctx_dict(request):
    ctx = {}
    ctx['categories'] = Category.objects.all()
    return ctx
