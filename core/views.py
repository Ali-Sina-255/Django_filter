from django.shortcuts import render
from . models import Book

from .filter import BookFilters

# Create your views here.
def index_view(request):
    book_filters = BookFilters(request.GET,queryset=Book.objects.all())
    # form = BookNameFilterForm()
    form = book_filters.form
    context = {
        "form":form,
        "books":book_filters.qs
    }
    return render(request, 'index.html',context)