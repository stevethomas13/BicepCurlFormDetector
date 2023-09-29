from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


app_name = "main"

urlpatterns = [
    path( "", views.index, name='index' ),
    path( "form", views.form, name='form'),
    path( "onboard", views.onboarding, name='onboard'),
    path( "detect", views.detect, name="detect")
]

urlpatterns += staticfiles_urlpatterns()