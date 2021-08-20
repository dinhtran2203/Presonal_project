from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Homepage_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def Contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def About_view(request, *args, **kwargs):
	my_context = {
		"my_text": "this is about me",
		"my_num" : "123"
	}

	return render(request, "about.html", my_context)

def Project_view(request, *args, **kwargs):
	return render(request, "project.html", {})
