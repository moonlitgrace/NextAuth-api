from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes.as_view()),
    path('signup/', views.SignupView.as_view()),
    path('all/', views.AllUsers.as_view()),
    path('current-user/', views.CurrentUser.as_view()),
    path('change-password/', views.changePasswordView.as_view()),

    # feedback
    path('new-feedback/', views.NewFeedback.as_view(), name='new-feedback'),
]