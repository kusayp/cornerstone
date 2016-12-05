from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import *
from home.models import Pastor
from django.conf import settings

# Create your views here.
def wwb(request):
	wwbs = WWB.objects.order_by('-id')
	paginator = Paginator(wwbs, 15)
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
		'wwbs': sermons_page,
		'title': 'What We Believe',
		}
		return render(request, 'wwb_ajax.html', context)
	context = {
		'wwbs': sermons_page,
		'title': 'What We Believe',
		'api_token': settings.API_KEY,
	}
	return render(request, 'wwb.html', context) 

# def wwb_detail(request, wwb_id):
# 	wwbs = get_object_or_404(WWB, pk=wwb_id)
# 	context = {
# 		'wwbs': wwbs,
# 		'title':'What We Believe',
# 	}
# 	return render(request, 'wwb_detail.html', context)

def message(request):
	messages = Message.objects.order_by('-id')[:1]
	questions = Question.objects.order_by('-id')
	context = {
		'messages' : messages,
		'questions': questions,
		'title': 'Welcome Message',
	}
	return render(request, 'message.html', context)

def about(request, slug):
	abouts = get_object_or_404(About, slug=slug)

	context = {
		'abouts' : abouts,
		'title' : 'About Us',
	}
	return render(request, 'about.html', context)

def leaders(request):
	leaders = Pastor.objects.order_by('id')[3:]

	context = {
		'leaders' : leaders,
		'title': 'Our Ministry Leaders',
	}
	return render(request, 'leaders.html', context)

def registration(request):

	context = {
		'title': 'Registration Page',
	}
	return render(request, 'registration.html', context)