Include the app's URLs in the project's URL patterns
• Open the urls.py file in your project's directory (e.g., fullstack_project/urls.py). 
• Import the include function from django. urls and the path function from django. urls:
• Add a new URL pattern to the urlpatterns list

from django.urls import include, path [if does not exits]




path('', include(portfolioapp.urls')),
