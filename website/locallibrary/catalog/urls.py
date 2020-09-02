from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('details' , views.details , name='details') ,
    
    
    path('' , views.sub , name='sub') ,
    
    path('sub' , views.sub , name='sub') ,
    path('log' , views.log , name='log') ,
    path('notuploc' , views.notuploc , name='notuploc') ,
    path('notupphoto' , views.notupphoto , name='notupphoto') ,
   
    path('action' , views.action , name='action') ,
    path('locations' , views.locations , name='locations') ,
    path('temperature' , views.temperature , name='temperature') ,
   
    path('ref' , views.ref , name='ref') ,
    path('photo' , views.photo , name='photo') ,
    path('profile', views.profile, name='profile'),
    
   
    
    
]
