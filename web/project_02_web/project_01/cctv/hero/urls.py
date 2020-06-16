from django.urls import path
from . import views

urlpatterns = [
    path('main_vis', views.main_vis, name="main_vis"),
    path('main_pct', views.main_pct, name="main_pct"),
    path('main_allstar', views.main_allstar, name="main_allstar"),
    path('r_1', views.r_1, name="r_1"),
   path('r_2', views.r_2, name="r_2"),
   path('r_3', views.r_3, name="r_3"),
   path('r_4', views.r_4, name="r_4"),
   path('r_5', views.r_5, name="r_5"),
   path('r_5_2', views.r_5_2, name="r_5_2"),
   path('r_6', views.r_6, name="r_6"),
   


   
    
    
]
