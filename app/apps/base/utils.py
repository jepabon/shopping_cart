from django.core.mail import EmailMultiAlternatives

def sent_email(subject, to, content, files=None):
    msg = EmailMultiAlternatives(subject, content, 'jepabon922@gmail.com', to)
    if files:
        for file in files:
            msg.attach_file(file)

    msg.send()
