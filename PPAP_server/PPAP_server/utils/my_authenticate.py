import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from user.models import User

UserModel = get_user_model()

class Myauthenticate(ModelBackend):
    #重写authenticate()方法，实现多形式账号登录，需要在dev.py配置，作为认证后端
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            if re.match(r'^1[3-9]\d{9}$',username):#手机号登录
                print("mmmmmmmm")
                user = User.objects.get(mobile=username)
            elif re.match(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',username):
                user = User.objects.get(email=username)#邮箱登录
                print("eeeeeeee")
            else:
                print("uuuuuuuuuu")
                user = User.objects.get(account=username)#用户名登录
        except Exception as e:
            return None
        else:
            if user.check_password(password):
                return user
            else:
                return None