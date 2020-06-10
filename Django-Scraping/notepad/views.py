from django.shortcuts import render, redirect
from .forms import NoteModelForm
from .models import Note
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

class NoteDetailView(DetailView):
    model = Note
    

class NoteListView(ListView):
    model = Note
    template_name = 'notepad/list.html'



class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'image', 'url']


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'image', 'url']


class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/home/'