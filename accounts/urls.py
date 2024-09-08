from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.SignupView.as_view()),
    # path("/login", views.SignupView.as_view())
]
