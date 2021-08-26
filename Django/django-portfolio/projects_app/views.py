from django.shortcuts import render

from .models import Projects
# Create your views here.
def  data_detail_view(request):
	obj = Projects.objects.get(id=1)
	context = {
		'title': obj.title,
		'description': obj.description
	}
	return render(request, "product/detail.html", context)

