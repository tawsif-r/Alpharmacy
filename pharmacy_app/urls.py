from django.urls import path



#importing person_view from views.py
from . import views

urlpatterns = [
    path('',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),# name="dashboard" allows us to use the tag in url in href
    path('medicines/',views.medicines,name='medicines'),
    path('customers/<str:pk>/',views.customers,name="customers"),
    path('create_order/<str:pk>/',views.createOrder,name='create_order'),
    path('create_medicine/',views.createMedicine,name='create_medicine'),
    path('update_order/<str:pk>/',views.updateOrder,name='update_order'), #making it dynamic
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
    

]
