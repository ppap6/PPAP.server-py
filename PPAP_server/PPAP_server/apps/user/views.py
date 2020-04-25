from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Helloviews(View):
    def get(self, request):
        return HttpResponse('hello', status=200)
