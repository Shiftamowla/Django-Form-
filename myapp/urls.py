from django.urls import path
from myapp.views import *

urlpatterns = [
    path('usershow/', usershow,name='usershow'),
    path('delete/<int:id>', delete,name='delete'),
    path('update/<int:id>', update,name='update'),
    path('userview/', userview,name='userview'),
]