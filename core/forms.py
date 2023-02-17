from django import forms
from core.models import Book


class BookForm(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Book
        fields = "__all__"
