from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("products/", views.products, name="products"),
    path("productDetail/<id>", views.product, name="product"),
    path("categoryDetail/<id>", views.category_products, name="category_products"),
]
