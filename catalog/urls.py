from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/', views.MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
    path('director/', views.DirectorListView.as_view(), name='director'),
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name='director-detail'),
]
