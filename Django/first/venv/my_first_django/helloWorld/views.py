from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'hello/index.html')

def home_view(request, *args, **kwargs):
	return render(request, "")