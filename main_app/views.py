from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Mod
from .forms import ShowForm

# Create your views here.

def home(request):
  return render (request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars})

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  id_list = car.mods.all().values_list('id')
  mods_car_doesnt_have = Mod.objects.exclude(id__in=id_list)
  show_form = ShowForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'show_form': show_form,
    'mods': mods_car_doesnt_have
  })


def add_show(request, car_id):
  form = ShowForm(request.POST)
  if form.is_valid():
    new_show = form.save(commit=False)
    new_show.car_id = car_id
    new_show.save()
  return redirect('detail', car_id=car_id)

def assoc_mod(request, car_id, mod_id):
  Car.objects.get(id=car_id).mods.add(mod_id)
  return redirect('detail', car_id=car_id)



class CarCreate(CreateView):
  model = Car
  fields = 'brand', 'model', 'description', 'year'

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

#CBV fors the car Mods
class ModList(ListView):
  model = Mod

class ModDetail(DetailView):
  model = Mod

class ModCreate(CreateView):
  model = Mod
  fields = '__all__'

class ModUpdate(UpdateView):
  model = Mod
  fields = ['name', 'type']

class ModDelete(DeleteView):
  model = Mod
  success_url = '/mods/'