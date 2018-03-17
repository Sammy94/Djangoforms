from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Album, Song
from django.template import loader

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.



class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = "all_album"

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'blog/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre']