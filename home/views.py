from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from events.models import Event
from aboutus.models import About
# from .forms import *

# Create your views here.


def home(request):
	welcome = Welcome.objects.order_by('-id')[:1]
	abouts = About.objects.order_by('-id')[:1]
	verse = Verse.objects.order_by('-id')[:1]
	pastors = Pastor.objects.order_by('id')[:3]
	events = Event.objects.order_by('-id')[:1]

	if request.method == 'POST':
		# form = SubscribeForm(request.POST) 
		email = request.POST['email']
		
		email = Subscribe.objects.create(email=email)
		email.save()
		return HttpResponse('')
	# else:
		# form = SubscribeForm()

	context = {
		# 'form':form,
		'events' : events,
		'abouts' : abouts,
		'verse' : verse, 
		'welcome' : welcome,
		'pastors' : pastors,
		'title': 'Home',
	}
	return render(request, 'home.html', context)

def pastor(request, pastor_id):
	pastors = get_object_or_404(Pastor, pk=pastor_id)
	pastor = Pastor.objects.order_by('id')[:3]

	context = {
		'pastors' : pastors,
		'pastor' : pastor,
		'title' : 'Our leaders',
	}
	return render(request, 'pastors.html', context)


