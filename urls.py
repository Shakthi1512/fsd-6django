Map the view function to a URL
• Open the urls.py file in your Django app's directory (e.g., listfruitapp/urls.py).
• Import the view function at the top of the file
• Add a new URL pattern to the urlpatterns list


from django.urls import path
from . import views
urlpatterns = [
path('main/', views.main, name='main'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
]
