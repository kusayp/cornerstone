from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from events.forms import *
from events.models import *
 
# Create your views here.
def event(request): 
	events = Event.objects.order_by('-id')
	categories = Category.objects.order_by('title')
	context = {
		'events' : events,
		'title': 'Events',
		'categories' : categories,
		'word': Word.objects.order_by('-id')[:1],
	}
	return render(request, 'event.html', context)

def event_detail(request, event_id):
	events = get_object_or_404(Event, pk=event_id)
	categories = Category.objects.order_by('title')
	form = RegisterForm()
	if request.method == 'POST': 
		# form = RegisterForm(request.POST)
		# if form.is_valid:
		# 	instance = form.save(commit=False)
		# 	instance.event = events
		# 	instance.save()
			# return HttpResponseRedirect('/resources/sermon/')

	# else:
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		
		email = Register.objects.create(name=name, email=email, phone=phone, event=event_id)
		email.save()
		return HttpResponse('')

		
	context = {
		'events' : events,
		'categories': categories,
		'form': form,
		'title': 'Events',
		'word': Word.objects.order_by('-id')[:1],
	} 
	return render(request, 'event_detail.html', context)

def categories_detail(request, title):
	events = Event.objects.all()
	categorys = Category.objects.order_by('title')
	category = get_object_or_404(Category, title=title)
	categories = events.filter(category=category)
	paginator = Paginator(categories, 2)
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
		'category' : categorys,
		'categorys': sermons_page,
		'word': Word.objects.order_by('-id')[:1],
		'title': 'Events',
		}
		return render(request, 'ajax.html', context)
	context = {
		'category' : categorys,
		'categorys': sermons_page,
		'word': Word.objects.order_by('-id')[:1],
		'title': 'Events',
	}
	return render(request, 'category_detail.html', context)