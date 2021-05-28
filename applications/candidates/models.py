


from model_utils.models import TimeStampedModel
from django.db import models

#cloudinary
from cloudinary.models import CloudinaryField

import pathlib

# Create your models here.

class Candidate(TimeStampedModel):
    names = models.CharField(max_length = 50)
    surnames = models.CharField(max_length = 50)
    education = models.CharField(max_length = 255, blank=True)
    country = models.CharField(max_length=30, blank=True)
    career_path = models.TextField(blank=True)
    political_party = models.CharField(max_length = 100)
    photo = CloudinaryField('photo')
    #photo = models.ImageField(default='null', upload_to="media/candidate-photos")
    photo_political_party = CloudinaryField('photo_political_party')
    #photo_political_party = models.ImageField(default = 'null', upload_to="media/political-party")

    def __str__(self):
        return self.names + ' ' + self.surnames

""" 
   web to get candidates -   https://andina.pe/agencia/noticia-elecciones-2021-revisa-aqui-los-perfiles-los-candidatos-presidenciales-831883.aspx


    voto informado -    https://votoinformado.jne.gob.pe/voto/Home/Busqueda

 """
route = str(pathlib.Path().absolute()) 
print('--------------', route)