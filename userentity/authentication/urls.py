from django.urls import path
from .views import ResetPassTODB, UserView,RegisterView,LogInView,LogOutView,SendResetPassEmail

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import ( 
    TokenRefreshView,
)
from django.contrib.auth import views


urlpatterns=[
    path("users/",UserView.as_view(),name="users"),

    # api for users activity
    path('users/API/login/',
        LogInView.as_view(),
        name = "login"
    ),
    path('users/API/logout/',
        LogOutView.as_view(),
        name="logout"
    ),
    path('users/API/register/',
        RegisterView.as_view(),
        name="register"
    ),
    path('users/API/token/refresh/',
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),


    # password reset
    path("users/API/password_reset/", 
        SendResetPassEmail.as_view(), 
        name="password_reset"),
    path(
        "users/API/reset/<uidb64>/<token>/",
        ResetPassTODB.as_view(),
        name="password_reset_confirm",
    ),

    
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
     path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
]
