from django import forms
from apps.core.models import Book,Paper,Event


class BookForm(forms.ModelForm):
    file = forms.FileField(required=False)
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
