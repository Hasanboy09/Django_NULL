from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models import Films, Genres
from apps.serializers import FilmModelSerializer, GenreSerializer


def hello_world_view(request):
    return HttpResponse("Hello, World!")


@extend_schema(tags=["Genre"])
class GenreListApiView(ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


@extend_schema(tags=["Films"])
class FilmstListView(ListCreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmModelSerializer
