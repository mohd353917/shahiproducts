from django.urls import path
from home import views

urlpatterns = [
    path("", views.index),
    path("about", views.about),
    path("contact-us", views.contact_us),
    path("login", views.Login),
    path("faq", views.faqs),
    path("ShahiSociety", views.shahi_society),
    path("turmeric", views.turmeric),
]
