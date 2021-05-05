from django.shortcuts import render
from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import approvals
from .serializers import approvalsSerializers
import pickle
import joblibs
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers

def myform(request):
    if request.method == 'POST':
        form = MyForm(request.POST)