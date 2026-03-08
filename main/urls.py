from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
        path('', views.main_info, name='info'),
        path('About', views.main_about, name='about'),
        path('Challenges', views.main_challenges, name='challenges'),  
]