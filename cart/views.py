from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Cart
from catalog.models import Book
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


class CartView(TemplateView):

    @method_decorator(login_required())
    def get(self, request, id):
        book = Book.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart.products.add(book)

        return HttpResponseRedirect(request.path_info)