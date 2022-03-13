from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

class User(View):
    def get(self,request):
        info = [
            {"name":"zhangsan","age":18},
            {"name": "lisi", "age": 8},
            {"name":"jsiks","age":28},
            {"name": "das", "age": 38},
            {"name": "da", "age": 48},

        ]
        return JsonResponse(info,safe=False)