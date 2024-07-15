from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[
    path('',login,name='login'),
    path('home/',home,name='Home'),
    path('Abouts/',about,name='Abouts'),
    path('Bookings/',booking,name='Bookings'),
    # path('Departments/',department,name='Departments'),
    path('Doctor/',doctor,name='Doctors'),
    path('Pharmacy/',pharmacy,name='Pharmacy'),
    path('Contact us/',contact,name='Contact'),
    path('Departments/',Tasklistview.as_view(),name='Departments'),
    path('deptdetail/<int:pk>',TaskDetailview.as_view(),name='cbvdetail'),
    path('deptupdate/<int:pk>',TaskUpdateview.as_view(),name='cbvupdate'),
    path('deptdelete/<int:pk>',TaskDeleteview.as_view(),name='cbvdelete'),
    path('logout/',logout,name='logout'),
  
    
]