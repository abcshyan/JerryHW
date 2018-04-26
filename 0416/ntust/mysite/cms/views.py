from django.shortcuts import render_to_response
from .models import Person
# Create your views here.

def index(request):
	person = Person.objects.all()
	return render_to_response('cms/website.html',locals())