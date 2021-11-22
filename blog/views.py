from django.shortcuts import get_object_or_404, render
from .models import Equipement
from .models import Animal

def post_list(request):
    equipements = Equipement.objects.all()
    animals = Animal.objects.all()
    return render(request, 'blog/post_list.html', {"animals": animals, "équimements":equipements})