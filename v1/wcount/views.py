from django.shortcuts import render
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return render(requests,'wcount/home.html',{'name':'pranith'})
def about(requests):
    return render(requests,'wcount/about.html',{'user id':'pranithbejugam'})
def hobbies(requests):
    return HttpResponse('<h1> Hobbies</h1><ol><li>Watching webseries</li></ol>')
