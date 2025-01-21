from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from pokedex.forms import PokemonForm, TrainerForm

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        }, 
     request))

def trainers(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainer_list.html')
    return HttpResponse(template.render({
        'trainers':trainers,
        },
        request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id = trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)  
        if form.is_valid():
             form.save()
             return redirect('pokedex:index')
    else:
            form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)  
        if form.is_valid():
             form.save()
             return redirect('pokedex:index')
    else:
            form = PokemonForm(instance=pokemon)
            
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
     template_name = "login_form.html"

#entrenador

@login_required
def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)  # El formulario para agregar un entrenador
        if form.is_valid():
            form.save()  # Guarda el nuevo entrenador
            return redirect('pokedex:trainers')  # Redirige a la lista de entrenadores
    else:
        form = TrainerForm()  # Muestra un formulario vacío
    return render(request, 'trainer_form.html', {'form': form})


@login_required
def edit_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)  # Obtiene el entrenador por ID

    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES, instance=trainer)  # Rellena el formulario con los datos existentes
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('pokedex:trainers')  # Redirige a la lista de entrenadores
    else:
        form = TrainerForm(instance=trainer)  # Si es un GET, muestra el formulario con los datos actuales

    return render(request, 'trainer_form.html', {'form': form})


@login_required
def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)  # Obtiene el entrenador por ID
    trainer.delete()  # Elimina el entrenador
    return redirect('pokedex:trainers')  # Redirige a la lista de entrenadores


    

    



    