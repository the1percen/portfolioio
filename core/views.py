from django.shortcuts import render, redirect
from .models import contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context=context)

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            
            html = render_to_string("newcontact.html",{
                'name':name,
                'email':email,
                'text':text,
            })
            
            send_mail('The contact form subject', 'This is the message', 'noreply@mohanrajlenova.com', ['mohanrajlenova@gmail.com'], html_message=html)
            form.save()            
            messages.info(request, "Message Sent Successfully")
            return redirect('contact')
    return render(request, "contact.html", {'form':form})

def work(request):
    context = {}
    return render(request, "work.html", context=context)

def legal(request):
    context = {}
    return render(request, "legal.html", context=context)

def f0f(request):
    context = {}
    return render(request, "404.html", context=context)