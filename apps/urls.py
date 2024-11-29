from django.urls import path

from apps.views import FilmstListView, GenreListApiView

urlpatterns = [
    path('genres', GenreListApiView.as_view() , name='genres'),
    path('films' , FilmstListView.as_view() , name='films' ),
]
