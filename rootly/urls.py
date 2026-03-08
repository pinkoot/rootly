from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Home/', include('main.urls')),
    path('About/', include('main.urls')),
    path('Challenges/', include('challenges.urls'))

]