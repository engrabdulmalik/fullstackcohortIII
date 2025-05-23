from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is my first django project")

def drinks(request,drink_name):
    
    drink={'mocha':'type of coffee',
           'tea':'type of hot beverage',
           'lemonade':'type of drink made from lemon juice',}
    choice_of_drink=drink[drink_name]
    return HttpResponse(f"<h1>{choice_of_drink}</h1> {drink_name}")