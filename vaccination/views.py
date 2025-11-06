from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
# request -> response
# request handler / view function
# action: render a template
def covid19_description(request):
    return render(request, 'staffs.html', {'name': 'Ryan Mark'})
    # pull data from database
    # Transform
    # send email
    # call external API