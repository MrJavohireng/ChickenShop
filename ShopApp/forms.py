from django import forms
from .models import Orders
class OrderForm(forms.Form):
    address=forms.CharField(widget=forms.TextInput(attrs={"class":"address", "placeholder":"Manzil"}))
    kg=forms.IntegerField( widget=forms.TextInput(attrs={"class":"kg", "placeholder":"Kilogram"}))
    price=forms.DecimalField(widget=forms.TextInput(attrs={"class":"price", "placeholder":"Narxi"}))
    debt=forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"debt"}), required=False)
    give=forms.DecimalField(widget=forms.TextInput(attrs={"class":"give", "placeholder":"Qancha berdi"}), required=False)