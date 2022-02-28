import permission as permission
from django.http import request
from django.shortcuts import render
from rest_framework .views  import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
f

# Create your views here.
class HelloView(APIView):
    permission.classes = (IsAuthenticated,)
    def get(self,request):
        content ={'message':"Hello,GeeksForGeeks"}
        return Response(content)

