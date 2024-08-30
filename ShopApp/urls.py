
from django.urls import path
from .views import MainPage, DetailOrderView, DeleteOrderView, CreateOrderView
app_name="ShopApp"
urlpatterns = [
    path("",MainPage.as_view(), name="main"),
    path("<int:pk>",DetailOrderView.as_view(), name="detail"),
    path("<int:pk>/delete/",DeleteOrderView.as_view(), name="delete"),
    path("create/",CreateOrderView.as_view(), name="create"),
]
