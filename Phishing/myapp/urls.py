from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [ 
    path('',views.index,name='index'),
    path('ind',views.ind,name='ind'),
    path('api',views.api,name='api'),
   
    path('search',views.search,name="search"),
    path('result',views.result,name='result'),
   
    
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
   
    path('geturlhistory',views.geturlhistory,name="geturlhistory"),
    path('page',views.page,name='page'),
    path('addcourse',views.addcourse,name="addcourse"),
   
    path('showblack',views.showblack,name="showblack"),
    path('updatee_view/<int:id>',views.updatee_view,name='updatee_view' ),
    path('de_view/<int:id>',views.de_view,name='de_view'),
  
]

