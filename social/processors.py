from .models import Social, Fact

def ctx_dict(request):
    ctx = {}
    socials = Social.objects.all()
    facts = Fact.objects.all()
    
    for link in socials:
        ctx[link.slug] = link.url
        
    for fact in facts:
        ctx[fact.slug] = fact.value
        
    return ctx