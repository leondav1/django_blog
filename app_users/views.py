from django.contrib.auth.views import LoginView, LogoutView


class LoginUserView(LoginView):
    template_name = 'users/login.html'


class LogoutUserView(LogoutView):
    template_name = 'users/logout.html'
