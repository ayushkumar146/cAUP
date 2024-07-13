from django.urls import path, include
from logreg.views import register_user, login_user, logout_user,makeup,makedown

urlpatterns = [
    # path("register/", register_user, name="register-user"),
    path("mylogin/", makeup, name="login-user"),
    path("myregister/", makedown, name="register-user"),
    # path("login/", login_user, name="login-user"),
    path("logout/", logout_user, name="logout-user"),
    path("home/",include("dashboard.urls")),
]