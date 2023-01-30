from django.contrib.auth.views import LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registro/logout.html')),
    path('signup/',views.register, name = 'register'),
    path('profile',views.profile_user,name='profile'),
    path('update/',views.update_user, name = 'update_user'),
    path('update-profile/',views.update_profile,name ='update-profile'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'registro/password_reset.html'),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = 'registro/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name = 'registro/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name = 'registro/password_reset_complete.html'),name='password_reset_complete'),
]