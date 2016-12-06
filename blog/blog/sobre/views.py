from django.shortcuts import render

from .models import SobreNos

# Create your views here.

def sobre_nos(request):
	sobre = SobreNos.objects.all()
	ctx = {'sobre': sobre}
	return render(request, 'sobre/sobre_nos.html', ctx)
	#return render(request, 'sobre/sobre_nos.html', {'sobre': sobre})