from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from PPAP_server.utils.mypagination import MyPageNumberPagination
from .models import User
from .serializers import UserSerializer
class Register(View):
    def get(self, request):
        # data = request.POST
        # account = data.name
        # password = data.password
        # email = data.email

        # if not all(account,password,email):
        #     return JsonResponse({"erromsg":"不能为空"}, status=400)

        return JsonResponse({"ok":1}, status=200)

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPageNumberPagination

    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs.pop("pk")
            data = request.data
            gender = data.get('gender')
            user_name = data.get('user_name')
            email = data.get('email')
            role_id = data.get('role_id')
            User.objects.filter(id=pk).update(gender=gender, user_name=user_name, email=email, role_id=role_id)
            # User.objects.filter(id=pk).update(**data)
            return Response({"status": 200,"message": "操作成功"})

        except:
            return Response({"status": 500,"message": "操作失败"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



