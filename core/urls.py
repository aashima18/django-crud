
from django.urls import path,include
from .views import indr, empdetail, empdelete, emp_create, empupdate



urlpatterns = [
    path('',indr,name="indr"),
    path('empdetail/<int:pk>',empdetail,name="empdetail"),
    path('empdetail/update/<int:pk>',empupdate,name="empupdate"),
    path('empdetail/delete/<int:pk>',empdelete,name="empdelete"),
    path('empdetail/create',emp_create,name='emp_create')
    
]
