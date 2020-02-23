from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [

    path('home/', views.home, name='start-home'),
    path('about/', views.about, name='start-about'),
    path('explore/', views.explore, name='start-explore'),
    path('account/', views.about, name='start-account'),
 
]
urlpatterns += staticfiles_urlpatterns()