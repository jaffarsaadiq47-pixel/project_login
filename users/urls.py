from django.urls import path # type: ignore
from .views import register, profile
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from .views import home, register, profile
urlpatterns = [
    path('', home),
    path('login/', TokenObtainPairView.as_view()),
    path('register/', register),
    path('profile/', profile),
]