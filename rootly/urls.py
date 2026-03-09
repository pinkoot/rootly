from django.contrib import admin
from django.urls import include, path
import uuid

urlpatterns = [
    path('', include('main.urls')),
    path('About/', include('main.urls')),
    path('Challenges/', include('challenges.urls'))

]