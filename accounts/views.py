from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, logout
from .serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User





class SignupView(APIView):

    def post(self,request):
        # 길이 유효성 검사
        def length_validation(char, field_name):
            if char is None:  
                return f"{field_name}는 필수 항목입니다."
            if len(char) > 30 or len(char) < 2 :
                return f"{field_name}는 2자 이상,30자 이하여야 합니다."
            
        errors = []

        # 유저네임 중복검사
        username = request.data.get("username")
        if User.objects.filter(username=username).exists():
            errors.append("이 username은 이미 사용 중입니다.")

        # 이메일 유효성 검사
        email = request.data.get("email")
        try:
            validate_email(email)
        except ValidationError:
            errors.append("이 이메일은 형식에 맞지 않습니다.")

        # 이메일 중복검사
        if User.objects.filter(email=email).exists():
            errors.append("이 이메일은 이미 사용 중입니다.")


        for field in ['username', 'password', 'email', 'name', 'nickname']:
            value = request.data.get(field)

            error = length_validation(value, field)
            if error:
                errors.append(error)

        # 에러가 있을 경우 응답 반환
        if errors:
            return Response({"errors": errors}, status=400)
        
        
    
        # 유저 생성
        user=User.objects.create_user(
            username = request.data.get("username"),
            name = request.data.get("name"),
            password = request.data.get("password"),
            email = request.data.get("email"),
            nickname = request.data.get("nickname"),
            birthday= request.data.get("birthday"),
            gender = request.data.get("gender"),
            introduction =request.data.get("introduction"),
            )
        
        return Response(f"{user.username}님 환영합니다!",status=201)           

class LoginView(APIView):
    def post(self,requset):
        username =requset.data.get("username")
        password =requset.data.get("password")
        user = authenticate(username=username,password=password)

        # 로그인 시 유저의 아이디, 비밀번호 확인
        if user is None:
            return Response({"error":"아이디 또는  비밀번호가 올바르지 않습니다."},status=400)
        
        res_data = UserSerializer(user).data
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)
        res_data["access_token"]= access_token
        res_data["refresh_token"]= refresh_token

        return Response(res_data)
    

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        check_user = request.user
        if check_user.username != username:
            return Response({"error":" 잘못된 접근 입니다."},status=403)
            
        user = User.objects.get(username=username)
        profile = UserSerializer(user)  

        return Response(profile.data, status=200)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)  
        return Response({"로그아웃 성공"}, status=204)