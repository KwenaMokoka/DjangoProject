from django.urls import path
from . import views


app_name = "parents"


urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
    path('about-us/', views.about_us_view, name='about_us'),
]
