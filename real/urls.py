from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.loginpage,name="login"),
    path('register/',views.registerUser,name='register'),
    path('management/',views.management,name='management'),
    path('delete/<str:id>',views.delcustomer,name='delcustomer'),
    path('logout/',views.logoutUser,name="logout"),
    path('customer<str:pk>',views.customer,name='customer'),
    path('',views.imghead1,name="home")
]