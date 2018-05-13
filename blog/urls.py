
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('index/',views.index,name="index"),
    # path('article/$',views.article_page, name = "article"),
    # path(r'^article/(?P<article_id>[0-9]+)$',views.article_page),
    path('article/<int:article_id>',views.article_page,name='article_page'),
    path('edit/',views.edit_page),
]
