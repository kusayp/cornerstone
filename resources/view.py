from django.shortcuts import render
from rest_framework import viewsets
from resources.serializers import *
from resources.models import *
from aboutus.models import *
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
# Create your views here.

class SermonViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all hymns
    """
    serializer_class = SermonSerializer
    queryset = Sermon.objects.all()

    
    @detail_route(methods=['get'])
    def comments(self, request, *args, **kwargs):
        this_sermon= self.get_object();
        comments=this_sermon.comments.all()
        stanzas_seria=SermonSerializer(comments, context={'request':request}, many=True)
        return Response({'results': stanzas_seria.data}, status= HTTP_200_OK)

class SermonCategoryViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all hymn categories
    """

    serializer_class = SermonCategorySerializer
    queryset = Tag.objects.all()

class SermonCommentViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all hymn categories
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Hymns ~ create hymns

        PARAMETERS:

        name , has_refrain, refrain, stanzas 

        """
        date_posted = request.data.get('date_posted')
        author = request.data.get('author')
        content = request.data.get('content')

        sermon = Sermon.objects.get(id=int(request.data.get('sermon')))
        
        print(request.data.get('sermon'))

        comments = Comment.objects.create(date_posted=date_posted, author=author, content=content, sermon=sermon)

            
        post = CommentSerializer(comments, context={'request': request}, many=False)
        return Response(post.data, status=HTTP_201_CREATED)


class DevotionViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all hymn categories
    """

    serializer_class = DevotionSerializer
    queryset = Devotion.objects.all()

class WwbViewSet(viewsets.ModelViewSet):

    """
    Returns a paginated list of all hymn categories
    """

    serializer_class = WwbSerializer
    queryset = WWB.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Hymns ~ create What we believe

        PARAMETERS:

        name , content

        """
        wwbs = request.data.get('results')
        for item in wwbs:
            title = item['title']
            content = item['content']

            wwb = WWB.objects.create(title=title, content=content)
        
        post = WwbSerializer(wwb, context={'request': request}, many=False)
        return Response(post.data, status=HTTP_201_CREATED)