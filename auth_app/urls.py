from django.urls import path
from .views import RegisterView,LoginView,LogoutView

urlpatterns = [
    path('reg/',RegisterView.as_view(),name="registerurl"),
    path('log/',LoginView.as_view(),name="loginurl"),
    path('logout/',LogoutView.as_view(),name="logouturl")
]