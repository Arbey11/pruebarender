from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contacto(request):
    if request.method=='POST':
        subject = request.POST['asunto']
        message = request.POST['mensaje'] + ' ' + request.POST['email']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['didier.garcia.galviz@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'respuesta_cliente.html')
    return render(request, 'contacto.html')