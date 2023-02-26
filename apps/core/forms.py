from django import forms
from apps.core.models import Book, Paper, Event, Contract, Plan, PlanApplication, Document, CostTopic, CostSection


class BookForm(forms.ModelForm):
    # file = forms.FileField(required=False)

    class Meta:
        model = Book
        fields = "__all__"


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = "__all__"


class EventForm(forms.ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = Event
        fields = "__all__"


class ContractForm(forms.ModelForm):
    document1 = forms.FileField(required=False)
    document1 = forms.FileField(required=False)
    document1 = forms.FileField(required=False)
    document1 = forms.FileField(required=False)

    class Meta:
        model = Contract
        fields = "__all__"


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"


class PlanApplicationForm(forms.ModelForm):
    class Meta:
        model = PlanApplication
        fields = "__all__"


class CostSectionForm(forms.ModelForm):
    class Meta:
        model = CostSection
        fields = "__all__"


class CostTopicForm(forms.ModelForm):
    class Meta:
        model = CostTopic
        fields = "__all__"



