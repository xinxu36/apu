from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['contactus@winningtodo.com']
            if cc_myself:
                recipients.append(sender)
                
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    
    return render_to_response('contact/contact.html', {
        'form' : form }, 
        )

def thanks(request):
    return render_to_response('contact/thanks.html')