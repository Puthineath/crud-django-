
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Staff
from django.urls import reverse


class StaffListView(ListView):
	model = Staff

# Create your views here.

class StaffCreateView(CreateView):
	model = Staff
	# fields = ('name', 'position')
	fields = ('__all__')

class StaffDetailView(DetailView):

	model = Staff
	def get_object(self,id):
		# id_ = self.kwargs.get("id")
		print(self.kwargs.get("id"))
		return get_object_or_404(Staff, id=id)

	# fields = ('__all__')
	"""docstring for ClassName"""
	
		

class StaffUpdateView(UpdateView):
	model = Staff
	# fields = ('name', 'position')
	fields = ('__all__')

	# def get_object(Self):
	# 	id_ = self.kwargs.get("id")
	# 	return get_object_or_404(Staff, id=id_)
