from rest_framework.serializers import ModelSerializer

from apps.models import Films, Genres


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class FilmModelSerializer(ModelSerializer):
    class Meta:
        model = Films
        fields =  '__all__'

    def to_representation(self, instance:Films):
        data = super().to_representation(instance)
        data['genres'] = GenreSerializer(instance.genres.all(), many=True).data
        return data
