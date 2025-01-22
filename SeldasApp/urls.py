from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.home,name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("order/", views.order, name="orderPage"),
    path("contact/", views.contact, name="contactPage"),
    path("shop/", views.shop, name="shopPage"),
    path("detail/<id>", views.detail, name="detailPage"),
    path("detailCat/<id>", views.detailCat, name="detailCatPage"),
    path("health/", views.health, name="healthPage"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]
