from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from . models import Group,GroupMembers
# Create your views here.

class CreatGroup(LoginRequiredMixin,generic.CreateView):
    fields = ['name', 'description']
    model = Group

class SingleGrou(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group
