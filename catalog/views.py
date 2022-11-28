from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        books = Book.objects.all()
        numb = books.count()
        authors = Author.object.all().count()


        return render(request, self.template_name, {'books': books, 'numb': numb, 'authors': authors})
