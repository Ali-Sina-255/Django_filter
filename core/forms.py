
import django_filters
from django import forms
from . models import Book


class BookFormsFilter(forms.ModelForm):
    class Meta:
        model = Book
        fields  = "__all__"