from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from social.models import Fact, Email

def contact(request):
	email_obj = Email.objects.get(id=1)
	correo_contacto = email_obj.email
	contact_form = ContactForm()
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		correo = request.POST.get('correo')
		contenido = request.POST.get('contenido')
		email = EmailMessage(
			"TU TIENDA, nuevo msj desde Contacto",
			"De {} <{}>\n\nMensaje: \n\n{}".format(nombre, correo, contenido),
			"no-responder@uverodev.com",
			[correo_contacto],
			reply_to=[correo]
		)
		try:
			email.send()
			return redirect(reverse('contacto')+"?send=ok")
		except:
			print
			return redirect(reverse('contacto')+"?send=ko")
		
	
	return render(request, 'contact/contact.html', {'form':contact_form})