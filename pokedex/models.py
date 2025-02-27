from django.db import models
# Creacion de la clase Trainer

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to="trainer_images", null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),   
    }
    type = models.CharField(max_length=30, choices= POKEMON_TYPES, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemon_images")
    

    def __str__(self):
        return self.name