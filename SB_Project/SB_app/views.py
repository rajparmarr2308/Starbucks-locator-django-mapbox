from django.shortcuts import render

# Create your views here.
from .forms import LocationForm
from .models import Location,City
def HomeView(request):
    context ={}
 
    # create object of form
    form = LocationForm(request.POST or None, request.FILES or None)
    all_locs=None
    if request.method=="POST":
        city_id =request.POST['city']
        print(city_id,"--------------------------")
        all_locs=Location.objects.filter(city_id=city_id)
        print(all_locs)
    context['form']=form
    context["locations"]=all_locs
    return render(request, "index.html",context)