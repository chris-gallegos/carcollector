from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

class Car:
    def __init__(self, brand, model, description, year):
        self.brand = brand
        self.model = model
        self.description = description 
        self.year = year

cars = {
    Car('Ford', 'Mustang', 'Fast and powerful', 2023),
    Car('Chevy', 'Camaro', 'discontinued', 2022),
    Car('Tesla', 'Model 3', 'Electric', 2019),
    Car('BMW', 'i8', 'Electric', 2018)
}

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', { 'cars': cars})