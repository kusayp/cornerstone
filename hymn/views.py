from django.shortcuts import render
from django.conf import settings 
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
def hymn(request):
	details = Hymn.objects.order_by('name')
	# categorys = Category.objects.order_by('name')
	# category = get_object_or_404(Category, name=name)
	# categories = details.filter(categorys=category)
	context = {
		'titles' : details,
		'title': 'Hymn',
		'api_token': settings.API_KEY,
	}
	return render(request, 'hymn_ls.html', context) 


def stanza_detail(request, hymn_id):

	    details = Hymn.objects.get(id = hymn_id)
	    has_refrain = details.has_refrain
	    refrain = details.refrain
	    stanza = details.stanzas.all()
	    context = {
    	'name' : details,
    	'hymn' : refrain,
    	'titles' : stanza,
    	'title': 'Hymn Details',
    	'has_refrain': has_refrain,
    	'api_token': settings.API_KEY,
    	}
	    return render(request, 'hymn.html', context)
