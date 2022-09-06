from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView

app_name = "account_app"
urlpatterns = [
    path('login', views.LoginFormView.as_view(), name='login'),

    path('forgot_password', views.ForgotPassword.as_view(), name='forgot_password'),

    path('password_reset_complete',
         views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),


]
