from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    # 注册
    url(r'^register/$', views.Register.as_view()),
    url(r'^user/login/$', obtain_jwt_token),
]

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(prefix='user',viewset=views.UserView, basename="user")
urlpatterns += router.urls