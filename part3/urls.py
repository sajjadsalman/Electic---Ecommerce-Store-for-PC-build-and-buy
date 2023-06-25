from django.contrib import admin
from django.urls import path
from part3 import views

urlpatterns = [
    path('components/', views.component_list, name='component_list'),
    path('', views.main_page, name='main_page'),
    path('computers/', views.computer_list, name='computer_list'),
    path('about/', views.about_page, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_thankyou/', views.feedback_thankyou, name='feedback_thankyou'),
    path('contact/', views.contact_page, name='contact'),
    path('computers/<int:computer_id>/swap/', views.swap_component, name='swap_component'),
    path('computers/<int:computer_id>/swap/order_summary/', views.order_summary, name='order_summary'),
    path('computers/<int:computer_id>/swap/order_summary/order_complete', views.order_complete, name='order_complete'),
]