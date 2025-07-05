from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True  # optional: skip login page if already logged in

    def get_success_url(self):
        return self.request.GET.get("next") or reverse("home")


class MyLogoutView(LogoutView):
    def get_success_url(self):
        return self.request.GET.get("next") or reverse("accounts:login")
