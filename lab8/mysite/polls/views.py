from django.shortcuts import render
from .models import Weapon

def gun1(request):
    gun = Weapon.objects.all()[0]
    return render(request, 'polls/paterson.html', {'gun': gun})
def gun2(request):
    gun = Weapon.objects.all()[1]
    return render(request, 'polls/kalashnikov.html', {'gun': gun})
def gun3(request):
    gun = Weapon.objects.all()[2]
    return render(request, 'polls/dragunov.html', {'gun': gun})

def main(request):
    return render(request, 'polls/index.html')
