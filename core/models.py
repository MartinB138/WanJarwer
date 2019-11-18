from django.db import models
from django.urls import reverse
# Create your models here.

class Proce(models.Model):
	
	proce = models.ForeignKey('Marca_Proce', on_delete=models.SET_NULL, null=True)
	proceN = models.CharField(max_length=50)
	core = models.CharField(max_length=3)
	threads = models.CharField(max_length=3)
	frecMini = models.CharField(max_length=4)
	frecMax = models.CharField(max_length=4)

	def __str__(self):
		return self.proceN

class Marca_Proce(models.Model):
	
	nom = models.CharField(max_length=10)

	def __str__(self):
		return self.nom

class Graph(models.Model):

    
    graph = models.ForeignKey('Marca_Graph', on_delete=models.SET_NULL, null=True)
    graphN = models.CharField(max_length=50)
    gb = models.CharField(max_length=2)
    frecMin = models.CharField(max_length=4)

    def __str__(self):
	    return self.graphN

class Marca_Graph(models.Model):
	
	nomg = models.CharField(max_length=10)

	def __str__(self):
		return self.nomg

class Ram(models.Model):
    
	marcr = models.CharField(max_length=10)
	nomr = models.CharField(max_length=30)
	gbs = models.CharField(max_length=2)
	frecMinn = models.CharField(max_length=5)
	volt = models.CharField(max_length=5)

	
	def __str__(self):
		return self.nomr

class Gab(models.Model):
    
	marca_gabinete = models.CharField(max_length=15)
	nombre_gabinete = models.CharField(max_length=40)
	tipo_gabinete = models.ForeignKey('Marca_Gab', on_delete=models.SET_NULL, null=True)


	def __str__(self):
		return self.nombre_gabinete
	
class Marca_Gab(models.Model):
	
	nomge = models.CharField(max_length=10)

	def __str__(self):
		return self.nomge