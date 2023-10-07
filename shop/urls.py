#from django.conf import settings
#from django.conf.urls.static import static
from django.urls import path 
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('fixed',views.fixed,name='fixed'),
    path('Nonfixed',views.Nonfixed,name='Nonfixed'),
    path('Statement',views.Statement,name='Statement'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about'),
]

#if settings.DEBUG:
 #   urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_)