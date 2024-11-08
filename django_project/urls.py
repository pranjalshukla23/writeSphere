"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # run the register function of users app when we hit "/register"
    path("register/", user_views.register, name="register"),
    # run the profile function of users app when we hit "/profile"
    # this is a protected route, you cannot access it until you login
    path("profile/", user_views.profile, name="profile"),
    # run the django´s built in login view when user hits "/login"
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    # run the django´s built in logout view when user hits "/logout"
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    # run the django´s built in password reset view when user hits "/password-reset"
    path('password-reset/', PasswordResetView.as_view(template_name="users/password_reset.html"), name='password_reset'),
    # run the django´s built in password reset done view when user hits "/password-reset/done/"
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),
    # run the django´s built in password reset confirm view when user hits "/password-reset-confirm"
    path('password-reset-confirm<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    # run the django´s built in password reset confirm view when user hits "/password-reset-confirm"
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
    # navigating to urls.py file of blog app
    path('', include('blog.urls')),
]

# for debug mode
if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


