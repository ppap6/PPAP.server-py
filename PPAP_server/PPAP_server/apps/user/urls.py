from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    # 注册
    url(r'^hello/$', views.Helloviews.as_view()),
]