from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('fake-data/<int:data>/', views.fake_data, name='fakedata'),
]