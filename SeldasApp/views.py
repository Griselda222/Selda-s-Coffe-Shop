from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

def order(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"products":products, "categories":categories}
    return render(request, "order.html", context)

def shop(request):
    factorys=Factory.objects.all()
    context={"factorys":factorys}
    return render(request, "shop.html",context)

def detail(request,id):
    productDetail=Product.objects.get(pk=id)
    context={"productDetail":productDetail}
    return render(request,"detail.html")
def detailCat(request, id):
    categories = Category.objects.all()
    categoryDetail = Category.objects.get(pk=id)
    productCategory = Product.objects.filter(product_category =categoryDetail)
    context = {"categoryDetail": categoryDetail, "categories":categories, "productCategory":productCategory}
    return render(request, "detailCat.html", context)

def contact(request):
    if request.method=="POST":
        firstName=request.POST["emri"]
        lastName=request.POST["mbiemri"]
        email=request.POST["email"]
        comment=request.POST["koment"]
        if firstName!="" and lastName!="" and email!="" and comment!="":
            Contact(contact_name=firstName,
                contact_surname=lastName,contact_email=email,contact_comment=comment).save()
            messages.success(request,"Thanks")
        else:
            messages.error(request,"Fill fields")
    return render(request,"contact.html")

def health(request):
    return render(request,"health.html")

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import your custom form

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

