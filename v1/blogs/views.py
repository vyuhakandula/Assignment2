from django.shortcuts import render
from django.http import HttpResponse
import operator

def drinks(requests):
    return HttpResponse('Drink 3L water everyday will keep you hydrated')
def foods(requests):
    return HttpResponse('Dont eat market food')

# Create your views here.
