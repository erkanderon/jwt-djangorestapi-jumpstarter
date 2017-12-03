from django.shortcuts import render
from utils.utils import *

# Create your views here.

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class TodoList(APIView):

    ##authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    ##authentication_classes = (JSONWebTokenAuthentication,)


    def get(self, request):
        pass

    def post(self, request):
        
        f = Todo.objects.all()
        serializer = TodoSerializer(f, many=True)
        return Response(responseSerializer(200, serializer.data))