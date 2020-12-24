from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm
from social.models import Fact, Email

def contact(request):
	email_obj = Email.objects.get(id=1)
	dato_email_asunto = Fact.objects.get(slug = "dato_email_asunto")
	correo_contacto = email_obj.email
	contact_form = ContactForm()
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		correo = request.POST.get('correo')
		contenido = request.POST.get('contenido')
		try:
			send_mail(
    			dato_email_asunto.value,
				"De {} <{}>\n\nMensaje: \n\n{}".format(nombre, correo, contenido),
    			correo_contacto,
    			[correo_contacto, correo],
    					fail_silently=False,
				)
			return redirect(reverse('contacto')+"?send=ok")
		except:
			print
			return redirect(reverse('contacto')+"?send=ko")
		
	
	return render(request, 'contact/contact.html', {'form':contact_form})