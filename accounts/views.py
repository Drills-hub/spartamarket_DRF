from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User



# Create your views here.
class SignupView(APIView):
    def post(self,request):

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        nickname = request.data.get("nickname")
        birthday= request.data.get("birthday")
        gender = request.data.get("gender")
        introduction =request.data.get("introduction")

        User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname,
            email=email,
            birthday=birthday,
            gender=gender,
            introduction=introduction,
            )

        return Response ({})                                   