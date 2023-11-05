from django.urls import path
from .import views
urlpatterns=[
    path("a/",views.index,name='index'),
    path("portfolio/",views.htmlexample,name='htmlexample'),
    path("blog/",views.blog,name='blog'),
    path("blog/read.html/",views.read,name='read'),
    path("resume/",views.resume,name='resume'),
    
]
