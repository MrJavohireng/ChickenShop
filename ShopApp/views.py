from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Orders
from django.http import HttpResponse
from .forms import OrderForm
from django.urls import reverse
from django.http import HttpResponseRedirect
class DetailOrderView(View):
    def get(self, request, pk):
        object=Orders.objects.get(pk=pk)
        context={"form":OrderForm(data={"address":object.address, "kg":object.kg, "price":object.price, "debt":object.debt, "give":object.give, }), "object":object,"remain":object.price-object.give,}
        return render(request=request, template_name="ShopApp/orders_detail.html", context=context)
    def post(self,request, pk):
        form=OrderForm(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            kg=form.cleaned_data["kg"]
            price=form.cleaned_data["price"]
            debt=form.cleaned_data["debt"]
            give=form.cleaned_data["give"]
            if debt is None:
                debt=False
            if give is None:
                give=0
            Orders.objects.filter(pk=pk).update(address=address,kg=kg,price=price,debt=debt,give=give)
        return HttpResponseRedirect(reverse("ShopApp:main"))
            

class MainPage(ListView):
    queryset=Orders.objects.all()
    context_object_name="orders"

class CreateOrderView(View):
    def get(self, request):
        form = OrderForm()
        return render(request=request, template_name="ShopApp/orders_create.html", context={"form":form,})
    def post(self, request):
        form=OrderForm(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            kg=form.cleaned_data["kg"]
            price=form.cleaned_data["price"]
            debt=form.cleaned_data["debt"]
            give=form.cleaned_data["give"]
            if debt is None:
                debt=False
            if give is None:
                give=0
            Orders.objects.create(address=address, kg=kg, price=price, debt=debt, give=give)
            
        return HttpResponseRedirect(reverse("ShopApp:main"))
    
    
class DeleteOrderView(View):
    def get(self, request, pk):
        object=Orders.objects.get(pk=pk)
        return render(request=request, template_name="ShopApp/orders_delete.html", context={"object":object,})
    def post(self, request, pk):
        object=Orders.objects.filter(pk=pk).delete()
        return HttpResponseRedirect(reverse("ShopApp:main"))