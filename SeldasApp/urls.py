from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.home,name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("order/", views.order, name="orderPage"),
    path("contact/", views.contact, name="contactPage"),
    path("factory/", views.factory, name="factoryPage"),
    path("detail/<id>", views.detail, name="detailPage"),
    path("detailCat/<id>", views.detailCat, name="detailCatPage"),
    path("health/", views.health, name="healthPage"),
]

