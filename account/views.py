from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, \
    PasswordChangeView

from django.shortcuts import render, redirect


#
#
from django.urls import reverse_lazy


from account.forms import UserLoginForm

from django.views.generic import View


class LoginFormView(View):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('index_app:index_url')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})



class ForgotPassword(PasswordResetView):
    template_name = 'account/forgotpassword.html'
    email_template_name = 'account/password_reset_email.html'

    success_url = reverse_lazy('index_app:index_url')


