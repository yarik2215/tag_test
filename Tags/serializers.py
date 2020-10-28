from django.db.models import fields
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth import get_user_model

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    childs = RecursiveField(allow_null=True, read_only=True, many=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'parrent', 'childs']


class UserSerializer(serializers.ModelSerializer):
    # tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = [ 'id', 'username', 'first_name', 'last_name', 'email']


class UserTagsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'tags']
        