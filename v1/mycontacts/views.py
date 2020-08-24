from django.shortcuts import render
from django.http import HttpResponse
import operator

def whoami(requests):
    return HttpResponse('Iam this.My email id is:bejugam2000@gmail.com')
def name(requests):
    return HttpResponse('My name is Pranith Kumar')
# Create your views here.
