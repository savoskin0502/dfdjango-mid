from rest_framework import serializers
from .models import Book, Journal
from auth_.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'role')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    publisher = UserSerializer(many=False)

    class Meta:
        model = Journal
        fields = ('id', 'name', 'price', 'description', 'created_at',
                  'type', 'publisher')
        depth = 2
