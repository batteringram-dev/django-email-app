from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings 

# Create your views here.

def email_api(request):
    send_email_from_app()
    data = {
        "success": True,
        "message": "sending email"
    }
    return JsonResponse(data)

def send_email_from_app():
    html_tpl_path = 'email_templates/welcome.html'
    context_data =  {'name': 'JK'}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = ''
    email_msg = EmailMessage('Welcome from django app', 
                                email_html_template, 
                                settings. APPLICATION_EMAIL,
                                [receiver_email],
                                reply_to=[settings.APPLICATION_EMAIL]
                                )
  
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)
