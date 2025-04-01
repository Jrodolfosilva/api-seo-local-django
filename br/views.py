from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import request
from rest_framework.request import HttpRequest
from rest_framework.response import Response
# Create your views here.

class Estados (APIView):

    def get (self, request: HttpRequest):
        
        return Response({"its": "okay"})
