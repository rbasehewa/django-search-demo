from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
# request -> response
# request handler / view function
# action: render a template
def covid19_description(request):
    return HttpResponse("Covid-19 Using Django Views and URLConfs Demo")
    # pull data from database
    # Transform
    # send email
    # call external API