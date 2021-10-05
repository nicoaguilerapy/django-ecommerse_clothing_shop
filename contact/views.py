from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm
from social.models import Fact, Email
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def contact(request):
	email_obj = Email.objects.get(id=1)
	dato_email_asunto = 'Contacto desde Pagina Web'
	correo_contacto = email_obj.email
	contact_form = ContactForm()
	if request.method == 'POST':
		nombre = request.POST.get('name')
		correo = request.POST.get('email')
		contenido = request.POST.get('message')
		try:
			send_mail(
    			dato_email_asunto,
				"De {} <{}>\n\nMensaje: \n\n{}".format(nombre, correo, contenido),
    			correo_contacto,
    			[correo_contacto, correo],
    					fail_silently=False,
				)

			return HttpResponse("Mensaje Enviado")
		except:
			return HttpResponse("Mensaje No Enviado")
		
	
	return render(request, 'contact/contact.html', {'form':contact_form})