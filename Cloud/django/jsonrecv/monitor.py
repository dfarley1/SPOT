from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.template import loader
import django

def index(request):
    #stupid cookie thing we have to have.
    csrf_token = django.middleware.csrf.get_token(request)
    #which HTML file should we use?
    template = loader.get_template('monitor.html')
    
    #Do stuff here, fill a dictionary object from the database
    dummyData = {'a':'1234', 'b':'5687', 'c':'9876543'}
    
    #put that data into the HTML's context
    context = {'testD': dummData}
    #render the HTML page
    return HttpResponse(template.render(context, request))