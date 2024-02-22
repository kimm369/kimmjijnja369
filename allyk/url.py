from django.urls import path

from allyk import views

urlpatterns = [
    path('', views.index, name='My_index'),
    path('contact/', views.contact, name='My_contact'),
    path('about/', views.about, name='My_about'),
    path('gallery/', views.gallery, name='My_gallery')

]
