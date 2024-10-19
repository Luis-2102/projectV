from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('pages-login/', views.pages_login, name='pages_login'),
    path('pages-register/', views.pages_register, name='pages_register'),
    path('product_list/', views.product_list, name='product_list'),
    path('users-profile/', views.users_profile, name='users_profile'),
]
