from rest_framework import serializers

from .models import Actor, Category, Director, Movie, Episode


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            "id",
            "name",
        ]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            "id",
            "name",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = [
            "name",
            "slug",
            "filename",
            "link_embed",
            "link_m3u8"
        ]

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "name",
            "origin_name",
            "description",
            "type",
            "status",
            "thumb_url",
            "poster_url",
            "on_theater",
            "trailer_url",
            "duration",
            "current_episode",
            "episode_total",
            "lang",
            "slug",
            "year",
            "country",
            "actors",
            "directors",
            "categories",
        ]

    def create(self, validated_data):
        actors = validated_data.pop('actors')
        directors = validated_data.pop('directors')
        categories = validated_data.pop('categories')
        movie_instance = Movie.objects.create(**validated_data)
        for actor_data in actors:
            Actor.objects.create(**actor_data)
        for director_data in directors:
            Director.objects.create(**director_data)
        for category_data in categories:
            Category.objects.create(**category_data)
        return movie_instance
