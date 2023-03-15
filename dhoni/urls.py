from dhoni.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('jinja_second/',jinja_second,name='jinja_second'),
]