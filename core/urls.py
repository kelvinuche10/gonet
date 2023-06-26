from django.urls import path
from . import views


urlpatterns = [
    path('<str:room/?username=username', views.RoomView.as_view, name='home'),
    path('', views.HomeView.as_view, name='home')
]