from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.decorators import action, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin, IsCompanyAdmin
from .models import Tag
from .serializers import TagSerializer, UserSerializer, UserTagsSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    # queryset = Tag.objects.filter(parrent__isnull=True)
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly] 
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = queryset = Tag.objects.filter(parrent__isnull=True)
        return super().list(self, request)


# class UserViewSet(viewsets.ModelViewSet):
#     model = queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminOrReadOnly]


class UserListView(APIView):

    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def get(self, request, format=None):
        users = get_user_model().objects.all()
        
        serializer = UserSerializer(users, many=True, context={'request':request})
        return Response(serializer.data , 200)


class UserTagsView(APIView):
    
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request, format=None):
        user_id = request.GET.get('user_id')
        if user_id:
            user = get_user_model().objects.get(pk=user_id)
        else:    
            user = request.user
        
        serializer = TagSerializer(user.tags, many=True, context={'request':request})
        return Response(serializer.data , 200)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
