from django.contrib import admin

# Register your models here.

from .models import Book , Paper , Event

admin.site.register(Book)
admin.site.register(Paper)
admin.site.register(Event)


