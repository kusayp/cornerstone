from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .forms import *
from .models import *


def contact(request):
    address = Address.objects.order_by('-id')[:1]
    form = ContactForm()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        email = Contact.objects.create(name=name, email=email, phone=phone, content=content)
        email.save()
        return HttpResponse('')

    context = {
        'form': form,
        'address': address,
        'title': 'Contact',
    }
    return render(request, "contact.html", context)


def handler404(request):
    response = render('404.html', {}, context=RequestContext(request))
    response.status_code = 404
    return response
