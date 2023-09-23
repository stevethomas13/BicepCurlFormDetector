from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


app_name = "main"

urlpatterns = [
    path( "", views.index, name='index' ),
    path( "form", views.form, name='form')
]

urlpatterns += staticfiles_urlpatterns()