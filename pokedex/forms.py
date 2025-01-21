from django import forms 
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type':'Tipo',
            'height': 'Altura',
            'weight': 'Peso',
            'trainer': 'Entrenador',
            'picture': 'Foto'
        }
        widgets =  {
             'name' : forms.TextInput(attrs={'class': 'form-control'}),  
             'type' : forms.Select(attrs={'class': 'form-control'}),
             'height' : forms.NumberInput(attrs={'class': 'form-control'}),
             'weight' : forms.NumberInput(attrs={'class': 'form-control'}),
             'picture' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
             'trainer' : forms.Select(attrs={'class': 'form-control'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'age': 'Edad',
            'date': 'Fecha Nacimiento'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }

    