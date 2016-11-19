from rest_framework import serializers
from users.models import PCUser
from users.serializers import UserSerializer
from hymn.models import *
from django.contrib.auth import get_user_model
from events.models import *
 
class StanzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanza
        fields = ('id', 'content',)

class HymnSerializer(serializers.ModelSerializer):
    stanzas = StanzaSerializer(many=True)
    class Meta:
        model = Hymn
        fields = ('id', 'name', 'has_refrain','refrain','stanzas',)

class CategorySerializer(serializers.ModelSerializer):
    hymns = HymnSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'hymns',)

class EventSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Event
        fields = ('id', 'organizer', 'details','name','location',)

class RegisterSerializer(serializers.ModelSerializer):
    event =EventSerializer(many=False)
    class Meta:
        model = Register
        fields = ('id','name','event','phone', )
