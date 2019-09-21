from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='index'),
    path('audio',views.audio,name='audio')
]
