from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from events.models import Word

# Create your views here.
def sermon(request):
	sermons = Sermon.objects.order_by('-id')
	categorys = Tag.objects.order_by('name')
	paginator = Paginator(sermons, 2)
	page = request.GET.get('page')
	try:
		sermons_page = paginator.page(page)
	except PageNotAnInteger:
		sermons_page = paginator.page(1)
	except EmptyPage:
		sermons_page = paginator.page(paginator.num_pages)
	context = {
		'sermons' : sermons_page,
		'categorys' : categorys,
		'title': 'Sermons',
		'api_token': settings.API_KEY, 
	}
	return render(request, 'sermon/sermon.html', context)


def sermon_detail(request, sermon_id):
	sermon = get_object_or_404(Sermon, pk=sermon_id)
	comments = sermon.comments.all()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid:
			instance = form.save(commit=False)
			instance.sermon = sermon
			instance.save()
			# return HttpResponseRedirect('/resources/sermon/')

	else:
		form = CommentForm()
	context = {
		'sermons' : sermon,
		'form': form,
		'comments' : comments,
		'title': 'Sermon Detail',
	}
	return render(request, 'sermon/sermon_detail.html', context)

def category_detail(request, name):
	sermons = Sermon.objects.all()
	categorys = Tag.objects.order_by('name')
	category = get_object_or_404(Tag, name=name)
	categories = sermons.filter(categorys=category)
	paginator = Paginator(categories, 2)
	page = request.GET.get('page')
	try:
		sermons_page = paginator.page(page)
	except PageNotAnInteger:
		sermons_page = paginator.page(1)
	except EmptyPage:
		sermons_page = paginator.page(paginator.num_pages)
	context = {
		'category' : categorys,
		'categorys': sermons_page,
		'title': 'Sermons',
		'word': Word.objects.order_by('-id')[:1],
		'api_token': settings.API_KEY,
	}
	return render(request, 'sermon/category_detail.html', context)

def devotion(request):
	devotions = Devotion.objects.order_by('-id')[:1]
	context = {
		'devotions' : devotions,
		'title': 'Devotions',
	}
	return render(request, 'devotion/devotion.html', context)
