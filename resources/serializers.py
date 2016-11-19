from rest_framework import serializers
from users.models import PCUser
from users.serializers import UserSerializer
from .models import *
from aboutus.models import *
from django.contrib.auth import get_user_model

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'sermon', 'date_posted', 'author', 'content',)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'date_posted', 'author', 'content',)

class SermonSerializer(serializers.ModelSerializer):
    comments =CommentSerializer(many=True)
    class Meta:
        model = Sermon
        fields = ('id', 'date_posted', 'title', 'date', 'author', 'content', 'comments',)

class SermonCategorySerializer(serializers.ModelSerializer):
    sermons = SermonSerializer(many=True)
    class Meta:
        model = Tag
        fields = ('id', 'name', 'sermons',)
 
class DevotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devotion
        fields = ('id', 'date_posted', 'title', 'content', 'principle',)

class WwbSerializer(serializers.ModelSerializer):
    class Meta:
        model = WWB
        fields = ('id', 'title', 'date', 'content',)