from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

class Staff(models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	age = models.PositiveIntegerField()

	def __str__(self):
		return  self.name + ":" + self.position
		

	def get_absolute_url(self):
		return reverse_lazy("staff_list", kwargs={"id": self.id})

	# def get_absolute_url(self):
	# 	return reverse_lazy("staff_create")


# Create your models here.
