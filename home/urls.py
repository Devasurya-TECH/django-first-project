from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='home'),

    path('about/', views.about, name='about'),

    path('booking/', views.booking, name='booking'),

    path('appointments/',
    views.appointments,
    name='appointments'),

    path('update/<int:id>/',
    views.update,
    name='update'),

    path('delete/<int:id>/',
    views.delete,
    name='delete'),

    path('doctors/',
    views.doctors,
    name='doctors'),

    path('contact/',
    views.contact,
    name='contact'),

    path('services/',
    views.services,
    name='services'),

]