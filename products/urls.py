from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_items, name='manage_items'),
    path('create_bill/', views.create_bill, name='create_bill'),
    path('bill/<int:bill_id>/', views.bill_detail, name='bill_detail'),
]
