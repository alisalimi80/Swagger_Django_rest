from django.contrib import admin
from .models import Writer,Movie,Cast,Profile
# Register your models here.

admin.site.register(Writer)
admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Profile)
