from django.urls import path,include
from .views import*
from . import views 
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'User',UserViewSet)  

urlpatterns=[
    path('',include(router.urls)),
    path('',views.Home),
    path('alluser/',views.Auser,name="alluser"),
    path('Flip/',views.Flip,name="Flip"),
    path('Tour/',views.Tour,name="Tour"),
    path('Tour1/',views.Tour1,name="Tour1"),
    path("deposite/",views.Deposite,name='deposite'),
    path("Flipcard/",views.Flipcard,name='Flipcard'),
    path("dis/",views.Display,name='dis'),
]