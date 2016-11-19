from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def men(request):
	mens = Men.objects.order_by('-id')[:1]
	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid:
			instance = form.save(commit=False)
			instance.save()
			# return HttpResponseRedirect('/')

	else:
		form = DonationForm()
	context = {
		'mens' : mens,
		'form' : form,
		'title': 'Men Fellowship',
	}
	return render(request, 'men.html', context)


def women(request):
	womens = Women.objects.order_by('-id')[:1]
	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid:
			instance = form.save(commit=False)
			instance.save()
			# return HttpResponseRedirect('/')

	else:
		form = DonationForm()
	context = {
		'womens' : womens,
		'form' : form,
		'title': 'Women Fellowship',
	}
	return render(request, 'women.html', context)


def youth(request):
	youths = Youth.objects.order_by('-id')[:1]
	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid:
			instance = form.save(commit=False)
			instance.save()
			# return HttpResponseRedirect('/')

	else:
		form = DonationForm()
	context = {
		'youths' : youths,
		'form' : form,
		'title': 'Youth Fellowship',
	}
	return render(request, 'youth.html', context)


def children(request):
	childrens = Children.objects.order_by('-id')[:1]
	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid:
			instance = form.save(commit=False)
			instance.save()
			# return HttpResponseRedirect('/')

	else:
		form = DonationForm()
	context = {
		'childrens' : childrens,
		'form' : form,
		'title': 'Children Fellowship',
	}
	return render(request, 'children.html', context)
