from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from events.forms import *
from events.models import *
 
# Create your views here.
def event(request): 
	events = Event.objects.order_by('-id')
	# is_free = events.is_free
	paginator = Paginator(events, 3)
	page = request.GET.get('page')
	try:
		sermons_page = paginator.page(page)
	except PageNotAnInteger:
		sermons_page = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		sermons_page = paginator.page(paginator.num_pages)
	if request.is_ajax():
		context = {
		'categorys': sermons_page,
		}
		return render(request, 'ajax.html', context)
	context = {
		'title': 'Events',
		'categorys': sermons_page,
		'word': Word.objects.order_by('-id')[:1],
	}
	return render(request, 'event.html', context)

def event_detail(request, event_id):
	events = get_object_or_404(Event, pk=event_id)
	form = RegisterForm()
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		
		email = Register.objects.create(name=name, email=email, phone=phone, event=event_id)
		email.save()
		return HttpResponse('')

		
	context = {
		'events' : events,
		'form': form,
		'title': 'Events',
		'word': Word.objects.order_by('-id')[:1],
	} 
	return render(request, 'event_detail.html', context)