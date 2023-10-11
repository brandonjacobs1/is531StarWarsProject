from django.shortcuts import render, redirect
from starWars.models import Character
from starWars.forms import CharacterForm


# Create your views here.
def index(request):
    context = {'data': 'test render'}
    return render(request, 'starWars/index.html', context)


def uploadCharacters(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='../characterList')
    else:
        form = CharacterForm()
        context = {'form': form}
        return render(request, 'starWars/uploadCharacter.html', context)


def listCharacters(request):
    context = {'characters': Character.objects.all()}
    return render(request, 'starWars/listCharacters.html', context)
