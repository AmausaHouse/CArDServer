from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.loginview.as_view(), name="login"),
    path('signup', views.signupview.as_view(), name="singup"),
    path('user/', include('social_django.urls', namespace='social')),
    path('face/', views.findface.as_view(), name='hoge'),
    path('profile/', views.profile.as_view(), name='profile')
]