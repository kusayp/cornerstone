from django.shortcuts import render
from rest_framework import viewsets
from hymn.serializers import *
from hymn.models import *
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
from events.models import Register, Event
# Create your views here.

class HymnViewSet(viewsets.ReadOnlyModelViewSet):

    """
    Returns a paginated list of all hymns
    """
    serializer_class = HymnSerializer
    queryset = Hymn.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Hymns ~ create hymns

        PARAMETERS:

        name , has_refrain, refrain, stanzas

        """
        hymns = request.data.get('results')
        for item in hymns:
            name = item['name']
            # slug = item['slug']
            has_refrain = item['has_refrain']
            refrain = item['refrain']
            stanzas = item['stanzas']

            hymn = Hymn.objects.create(name=name, has_refrain=has_refrain, refrain=refrain)

            for stan in stanzas:
                stanza=Stanza.objects.create(content=stan['content'], hymn=hymn)

        
        post = HymnSerializer(hymn, context={'request': request}, many=False)
        return Response(post.data, status=HTTP_201_CREATED)

    @detail_route(methods=['get'])
    def stanzas(self, request, *args, **kwargs):
        this_hymn= self.get_object();
        comments=this_hymn.stanzas.all()
        stanzas_seria=StanzaSerializer(stanzas, context={'request':request}, many=True)
        return Response({'results': stanzas_seria.data}, status= HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all hymn categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class StanzaViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all stanzas
    """
    serializer_class = StanzaSerializer
    queryset = Stanza.objects.all()


class RegisterViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all stanzas
    """
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Hymns ~ create hymns

        PARAMETERS:

        name , has_refrain, refrain, stanzas

        """
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        
        event = Event.objects.get(id=int(request.data.get('event')))

        register=Register.objects.create(name=name, phone=phone, email=email, event=event)
        
        

        
        post = RegisterSerializer(register, context={'request': request}, many=False)
        return Response(post.data, status=HTTP_201_CREATED)


