from django.shortcuts import render
from .models import Movie, Director

def index(request):
    num_directors = Director.objects.all().count()
    num_movies = Movie.objects.all().count()
    return render(
        request,
        'index.html',
        context={
            # lo siguiente va a asociar las variables de esta
            # función, con elementos del index.html
            'num_movies' : num_movies,
            'num_directors' : num_directors
        }
    )

from django.views import generic

class MovieListView(generic.ListView):
    model = Movie

class MovieDetailView(generic.DetailView):
    model = Movie

class DirectorListView(generic.ListView):
    model = Director

class DirectorDetailView(generic.DetailView):
    model = Director
