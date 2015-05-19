from django.contrib import admin

from .models import Movie
from .models import Projection
from .models import Reservation

admin.site.register(Movie)
admin.site.register(Projection)
admin.site.register(Reservation)
