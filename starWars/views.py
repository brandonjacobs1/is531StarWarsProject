from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'data': 'test render'}
    return render(request, 'starWars/index.html', context)
