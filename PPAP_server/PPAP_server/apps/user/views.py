from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(View):
    def get(self, request):
        # data = request.POST
        # account = data.name
        # password = data.password
        # email = data.email

        # if not all(account,password,email):
        #     return JsonResponse({"erromsg":"不能为空"}, status=400)

        return JsonResponse({"ok":1}, status=200)

# class LoginView(APIView):
#     def post(self, request):
#         data = request.POST
#         account = data.email
#         pwd = data.password
#
#         if not all(account, pwd):
#             return Response({"message":"账号或者密码不能为空"},status=status.HTTP_406_NOT_ACCEPTABLE)
#
#         user = authenticate(request, )