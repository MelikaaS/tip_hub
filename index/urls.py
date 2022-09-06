from django.urls import path
from . import views

app_name='index_app'
urlpatterns=[
    path('index',views.index,name='index_url')
]