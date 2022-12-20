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
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    categories = CategorySerializer(many=True)
    episodes = EpisodeSerializer(many=True, write_only=True)

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
            "episodes",
        ]

    def create(self, validated_data):
        actors = validated_data.pop('actors')
        directors = validated_data.pop('directors')
        categories = validated_data.pop('categories')
        episodes = validated_data.pop('episodes')
        movie_instance = Movie.objects.create(**validated_data)
        for actor_data in actors:
            name = actor_data.get('name')
            try:
                actor_instance = Actor.objects.get(name=name)
            except Actor.DoesNotExist:
                actor_instance = Actor.objects.create(**actor_data)
            movie_instance.actors.add(actor_instance)
        for director_data in directors:
            name = director_data.get('name')
            try:
                director_instance = Director.objects.get(name=name)
            except Director.DoesNotExist:
                director_instance = Director.objects.create(**director_data)
            movie_instance.directors.add(director_instance)
        for category_data in categories:
            name = category_data.get('name')
            try:
                category_instance = Category.objects.get(name=name)
            except Category.DoesNotExist:
                category_instance = Category.objects.create(**category_data)
            movie_instance.categories.add(category_instance)
        for episode_data in episodes:
            Episode.objects.create(movie=movie_instance, **episode_data)
        return movie_instance
