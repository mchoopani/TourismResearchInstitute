from django.db import models
from apps.core.choices import *
from apps.core.serializers import Dictable
from multiselectfield import MultiSelectField


class Book(models.Model, Dictable):
    title = models.CharField(max_length=256, null=False)
    year = models.IntegerField(null=False)
    publisher = models.CharField(max_length=128, null=False)
    writers = models.CharField(max_length=256)
    specialized_field = models.IntegerField(default=0, choices=specialized_field_choices)
    book_type = models.IntegerField(default=0, choices=book_type_choices)
    research_group = MultiSelectField(max_length=3, choices=research_group_choices)
    ISBN = models.CharField(max_length=15, null=True)
    file = models.FileField(null=True)

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "publisher": self.publisher,
            "writers": self.writers,
            "specialized_field": self.specialized_field,
            "book_type": self.book_type,
            "research_group": self.research_group,
            "ISBN": self.ISBN,
            # "file": self.file.url,
        }

    @staticmethod
    def get_book_list(search_query=None):
        if search_query is None:
            return [book for book in Book.objects.all()]
        return [book for book in Book.objects.filter(title__contains=search_query)]

    @staticmethod
    def get_book_by_id(id):
        return Book.objects.get(id=id)
class Paper(models.Model):
    title = models.CharField(max_length=256, null=False)
    year = models.IntegerField(null=False)
    publisher = models.CharField(max_length=128, null=False)
    writers = models.CharField(max_length=256)
    specialized_field = models.IntegerField(default=0, choices=specialized_field_choices)
    book_type = models.IntegerField(default=0, choices=book_type_choices)
    research_group = MultiSelectField(max_length=3, choices=research_group_choices)
    ISBN = models.CharField(max_length=15, null=True)
    file = models.FileField(null=True)


    