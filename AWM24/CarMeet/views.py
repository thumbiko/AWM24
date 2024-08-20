from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from .models import Location


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('find_locations')
    else:
        form = UserCreationForm()
    return render(request, 'meetup/register.html', {'form': form})


@login_required
def find_locations(request):
    locations = Location.objects.all()
    return render(request, 'meetup/find_locations.html', {'locations': locations})


def get_locations(request):
    if request.method == 'GET':
        town = request.GET.get('town', None)
        if town:
            locations = Location.objects.filter(town__icontains=town)
        else:
            locations = Location.objects.all()

        locations_data = [{
            'name': loc.name,
            'lat': loc.coordinates.y,
            'lng': loc.coordinates.x
        } for loc in locations]

        return JsonResponse(locations_data, safe=False)
'''
def home(request):
    car_meets = CarMeet.objects.all()
    return render(request, 'carmeetapp/home.html', {'car_meets': car_meets})

def car_meet_detail(request, pk):
    car_meet = CarMeet.objects.get(pk=pk)
    return render(request, 'carmeetapp/car_meet_detail.html', {'car_meet': car_meet})
'''
