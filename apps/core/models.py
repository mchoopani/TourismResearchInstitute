from django.db import models
from apps.core.choices import *
from apps.core.serializers import Dictable
from multiselectfield import MultiSelectField


class Book(models.Model, Dictable):
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    publisher = models.CharField(max_length=128)
    writers = models.CharField(max_length=256)
    specialized_field = models.IntegerField(default=0, choices=specialized_field_choices)
    book_type = models.IntegerField(default=0, choices=book_type_choices)
    research_group = MultiSelectField(choices=research_group_choices,max_length=32)
    ISBN = models.CharField(max_length=15)
    file = models.FileField()
    created_on = models.DateTimeField(auto_now_add=True)


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
            "file": self.file.url,
            "created_on": self.created_on,
            "id": self.id,
        }

    @staticmethod
    def get_book_list(search_query=None):
        if search_query is None:
            return [book for book in Book.objects.all()]
        return [book for book in Book.objects.filter(title__icontains=search_query)]

    @staticmethod
    def get_book_by_id(id):
        return Book.objects.get(id=id)





class Paper(models.Model, Dictable):

    title = models.CharField(max_length=256)
    year = models.IntegerField()
    publisher = models.CharField(max_length=128)
    link = models.URLField(max_length=256)
    season = models.IntegerField(default=0, choices=season_choices)
    publish_number = models.IntegerField()

    research_group = MultiSelectField(max_length=3, choices=research_group_choices)
    specialized_field = models.IntegerField(default=0, choices=specialized_field_choices)

    corresponding_author = models.CharField(max_length=128)
    first_author = models.CharField(max_length=128)
    co_authors = models.CharField(max_length=128)
    type = models.IntegerField(default=0, choices=paper_type_choices)
    created_on = models.DateTimeField(auto_now_add=True)


    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "publisher": self.publisher,
            "co_authors": self.co_authors,
            "corresponding_author": self.corresponding_author,
            "first_authors": self.first_author,
            "link": self.link,
            "season": self.season,
            "publish_number": self.publish_number,
            "specialized_field": self.specialized_field,
            "research_group": self.research_group,
            "type": self.type,
            "created_on": self.created_on,
            "id": self.id
        }

    @staticmethod
    def get_paper_list(search_query=None):
        if search_query is None:
            return [paper for paper in Paper.objects.all()]
        return [paper for paper in Paper.objects.filter(title__icontains=search_query)]

    @staticmethod
    def get_paper_by_id(id):
        return Paper.objects.get(id=id)


class Event(models.Model, Dictable):
    title = models.CharField(max_length=256)
    date = models.DateField()
    research_group = MultiSelectField(max_length=32, choices=research_group_choices)
    specialized_field = models.IntegerField(default=0, choices=specialized_field_choices)
    file = models.FileField()

    type = models.IntegerField(default=0, choices=event_type_choices)

    instructor = models.CharField(max_length=256, null=True , blank=True)

    speaker = models.CharField(max_length=256, null=True , blank=True)
    scientific_director = models.CharField(max_length=256, null=True , blank=True)
    executive_director = models.CharField(max_length=256, null=True , blank=True)
    created_on = models.DateTimeField(auto_now_add=True )

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "specialized_field": self.specialized_field,
            "research_group": self.research_group,
            "instructor": self.instructor,
            "scientific_director": self.scientific_director,
            "executive_director": self.executive_director,
            "speaker": self.speaker,
            "file": self.file.url,
            "type": self.type,
            "created_on": self.created_on,
            "id": self.id,
        }

    @staticmethod
    def get_event_list(search_query=None):
        if search_query is None:
            return [event for event in Event.objects.all()]
        return [event for event in Event.objects.filter(title__icontains=search_query)]

    @staticmethod
    def get_event_by_id(id):
        return Event.objects.get(id=id)


class Contract(models.Model, Dictable):
    title = models.CharField(max_length=256, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.CharField(max_length=256, null=False)
    amount = models.PositiveBigIntegerField()
    cooperators = models.CharField(max_length=256)

    def to_dict(self):
        return {
            "title": self.title,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "manager": self.manager,
            "amount": self.amount,
            "cooperators": self.cooperators,
            "id": self.id,
        }

    @staticmethod
    def get_contract_list(search_query=None):
        if search_query is None:
            return [contract for contract in Contract.objects.all()]
        return [contract for contract in Contract.objects.filter(title__contains=search_query)]

    @staticmethod
    def get_contract_by_id(id):
        return Contract.objects.get(id=id)


class Plan(models.Model, Dictable):
    title = models.CharField(max_length=256, null=False)
    responsible_member = models.CharField(max_length=256, null=False)
    expiration_date = models.CharField(max_length=256, null=False)

    start_date = models.DateField()
    end_date = models.DateField()

    duration = models.CharField(max_length=256, null=False)
    amount = models.PositiveBigIntegerField()
    cooperators = models.CharField(max_length=512)
    specialized_field = models.IntegerField(default=0, choices=specialized_field_choices)
    research_group = MultiSelectField(max_length=32, choices=research_group_choices)
    created_on = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            "title": self.title,
            "responsible_member": self.responsible_member,
            "expiration_date": self.expiration_date,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "duration": self.duration,
            "amount": self.amount,
            "cooperators": self.cooperators,
            "specialized_field": self.specialized_field,
            "research_group": self.research_group,
            "created_on": self.created_on,
            "id": self.id,

        }

    @staticmethod
    def get_plan_list(search_query=None):
        if search_query is None:
            return [plan for plan in Plan.objects.all()]
        return [plan for plan in Plan.objects.filter(title__contains=search_query)]

    @staticmethod
    def get_plan_by_id(id):
        return Plan.objects.get(id=id)

    def get_document_set(self):
        return [doc for doc in self.document_set.all()]

    def get_application(self):
        return self.application


class Document(models.Model, Dictable):
    title = models.CharField(max_length=256, null=False)
    file = models.FileField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            "title": self.title,
            "file": self.file.url,
            "id": self.id

        }

    @staticmethod
    def get_document_by_id(id):
        return Document.objects.get(id=id)


class PlanApplication(models.Model, Dictable):
    income = models.PositiveBigIntegerField()
    total_income = models.PositiveBigIntegerField()
    total_cost = models.PositiveBigIntegerField()
    plan = models.OneToOneField(Plan,on_delete=models.CASCADE ,related_name='application')
    
    def to_dict(self):
        return {
            "income": self.income,
            "total_income": self.total_income,
            "total_cost": self.total_cost,
        }

    def get_topic_set(self):
        return [topic for topic in self.costtopic_set.all()]


class CostTopic(models.Model, Dictable):
    title = models.CharField(max_length=256, null=False)
    amount = models.PositiveBigIntegerField()
    plan_application = models.ForeignKey(PlanApplication, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "created_on": self.created_on,
            "id": self.id
        }

    def get_section_set(self):
        return [sec for sec in self.costsection_set.all()]
    @staticmethod
    def get_topic_by_id(id):
        return CostTopic.objects.get(id=id)


class CostSection(models.Model):
    title = models.CharField(max_length=256, null=False)
    amount = models.PositiveBigIntegerField()
    description = models.TextField(max_length=1024)
    topic = models.ForeignKey(CostTopic, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "description": self.description,
            "created_on": self.created_on,
            "id": self.id

        }
    @staticmethod
    def get_section_by_id(id):
        return CostSection.objects.get(id=id)


