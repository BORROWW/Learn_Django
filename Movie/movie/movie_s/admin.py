from django.contrib import admin

from .models import Category, Genre, Movie, Movie_Shot, Actor, RatingStar, Rating, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Movie_Shot)
admin.site.register(Actor)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
