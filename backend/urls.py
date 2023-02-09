from django.contrib import admin
from django.urls import path, include

from social_auth.views import GoogleLogin, GithubLogin

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # social links
    path('social-auth/google/', GoogleLogin.as_view(), name='google-login'),
    path('social-auth/github/', GithubLogin.as_view(), name='github_login'),
    # local links
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
