# Create your views here
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView

from .models import PetOwner, Pet

# Create your views here.
class Owners(View):
    def get(self, request):
        owners = PetOwner.objects.all()
        context = {"owners": owners}

        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))


# class OwnersList(TemplateView):
#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context, "ESTO VIENE DEL PADRE (TEMPLATEVIEW)")
#         context["owners"] = PetOwner.objects.all()
#         print(context, "ESTO LE AGREGAMOS NOSOTROS")
#         return context

# {% extends "base.html" %}

# {% block title %}
# <title>Pet Owner</title>
# {% endblock title %}

# {% block header %}
# <h1>Pet Owner detail</h1>
# {% endblock header %}

# {% block content %}

# <h1>Bienvenido {{ owner.first_name }}</h1>
# <p><strong>Name: </strong>{{ owner.first_name }} {{ owner.last_name }}</p>
# <p><strong>Address: </strong>{{ owner.address }}</p>
# <p><strong>Email: </strong>{{ owner.email }}</p>
# <p><strong>Phone: </strong>{{ owner.phone }}</p>

# {% endblock content %}
class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

# Pets View

class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"

class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"



