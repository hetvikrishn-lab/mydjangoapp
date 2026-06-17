from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview),
    path('home',views.homepageview),
    path('about',views.aboutpageview), 
    path('contact',views.contactpageview),
    path('contactprocess',views.contactprocess),
    path('cake',views.contactpageview),
    path('cake/ahmedabad',views.contactpageview),
    path('cake/rajkot',views.contactpageview),
    path('shop',views.shoppage), 
]