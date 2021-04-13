from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    # url(r'^register/$', views.Register.as_view()),
]
