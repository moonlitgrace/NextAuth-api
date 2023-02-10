from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings

class GoogleLogin(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

class GithubLogin(SocialLoginView):
    authentication_classes = []
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'https://nextauth-dj.vercel.app/'