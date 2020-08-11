from django.shortcuts import render

from rest_framework import generics

from .serializers import UsersProfile

from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import permissions


class ProfileView(generics.ListAPIView):
    serializer_class = UsersProfile
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()


class ProfileDetailView(generics.RetrieveAPIView):
    
    lookup_field = 'name'
    serializer_class = UsersProfile
    
    queryset = User.objects.all()




