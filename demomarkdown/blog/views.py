from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class BlogView(APIView):
    
    def get(self, request):
        DS = Blog.objects.all()
        serializer = BlogSerializer(DS, many=True)
        return Response(serializer.data)
    
    

