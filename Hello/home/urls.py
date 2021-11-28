from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.con, name='contact'),
    path("signup", views.handlesignup, name='signup'),
    path("login",views.handlelogin, name='login'),
    path("logout",views.handlelogout, name='logout'),
    path("homemadefood",views.homemadefood, name='homemadefood'),
    path("search", views.search, name='search'),
    path("tracker",views.tracker,name='tracker'),
    path("checkout",views.checkout,name='checkout'),
    path("productview/<int:id>",views.productview, name='productview')
]
