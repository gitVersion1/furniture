from django.shortcuts import render
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    products = Product.objects.all().order_by("-product_id")
    testimonials = Testimonial.objects.all()
    category = Category.objects.all().order_by("-pk")
    context = {"products": products, "testimonials": testimonials, 'category':category}
    return render(request, "home.html", context)


def contact(request):
    category = Category.objects.all().order_by("-pk")
    context = {'category':category}
    if request.method == "POST":
        inputName = request.POST['Fname']
        inputSurName = request.POST['Lname']
        inputEmail = request.POST['email']
        inputSMS = request.POST['sms']
        
        Contact(contact_name=inputName,
                contact_surname =inputSurName,
                contact_description = inputSMS,
                contact_email = inputEmail).save()
        messages.success(request, "SMS sended.")
        
    return render(request, "contact.html", context)


def products(request):
    category = Category.objects.all().order_by("-pk")
    products = Product.objects.all().order_by("-product_id")
    context = {"products": products, 'category':category}
    return render(request, "products.html", context)


def product(request, id):
    category = Category.objects.all().order_by("-pk")
    productDetail = Product.objects.get(product_id=id)
    context = {"productDetail": productDetail, 'category':category}
    return render(request, "product.html", context)


def category_products(request, id):
    category = Category.objects.all().order_by("-pk")
    categoryDetail = Category.objects.get(pk=id)
    categoryProduct = Product.objects.filter(product_category=categoryDetail)
    context = {"categoryDetail": categoryDetail, 'category':category, 'categoryProduct':categoryProduct}
    return render(request, "category_products.html", context)