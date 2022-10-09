from operator import length_hint
from django.shortcuts import render
import random
# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdeifghikjklmnopqrstz')
    generater_password = ''
    length =  int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMN'))

    if request.GET.get('special'):
        characters.extend(list('!@_-()[]/'))

    if request.GET.get('numbers'):
        characters.extend(list('01234567890'))


    for x in range(length):
        generater_password += random.choice(characters)


    return render(request, 'generator/password.html', {'password': generater_password})