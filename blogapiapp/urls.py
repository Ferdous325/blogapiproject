from django.urls import path
from . import views
urlpatterns = [
        path("articles/",views.articleList,name='articlelist'),
        path("articles/<slug:slug>",views.article_details,name="articledetails")
        
]
