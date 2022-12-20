from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    origin_name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    TYPE_CHOICES = [
        ('single', 'Single'),
        ('series', 'Series'),
    ]
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='si', null=True, blank=True)
    STATUS_CHOICES = [
        ('trailer', 'Trailer'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='t', null=True, blank=True)
    # single type -> duration: {duration} minutes
    # series type -> duration: {duration} minutes per a episode
    duration = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    on_theater = models.BooleanField(default=True, null=True, blank=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    # Vietsub or Narration or both
    lang = models.CharField(max_length=100, default='Vietsub', null=True, blank=True)
    current_episode = models.DecimalField(max_digits=4, decimal_places=0, default=0, null=True, blank=True)
    episode_total = models.DecimalField(max_digits=4, decimal_places=0, default=0, null=True, blank=True)
    trailer_url = models.CharField(max_length=511, null=True, blank=True)
    thumb_url = models.CharField(max_length=511, null=True, blank=True)
    poster_url = models.CharField(max_length=511, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')

    def __str__(self):
        return self.name

class Episode(models.Model):
    name = models.CharField(max_length=4, null=True, blank=True)
    slug = models.SlugField(max_length=4, null=True, blank=True)
    filename = models.CharField(max_length=255, null=True, blank=True)
    link_embed = models.CharField(max_length=511, null=True, blank=True)
    link_m3u8 = models.CharField(max_length=511, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
