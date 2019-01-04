from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    # Creating message subject and sender
    subject = 'Welcome to Accolade'
    sender = 'staceychebet23@gmail.com'

    #Context variables
    text_content = render_to_string('email/karibuemail.txt', {"name": name})
    html_content = render_to_string('email/karibuemail.html', {"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
