from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.explore, name='explore'),  # GET Request for Explore page
    path('dashboard/', views.dashboard, name='dashboard'),  # Main user dashboard page
    path('users/', include('django.contrib.auth.urls')),  # Auth user model
    path('register/', views.Register.as_view(), name='register'),  # CBV Test
    path('login/', views.get_login_form, name='login'),  # GET Request for login form
    path('login/auth/', views.authenticate_user, name='auth'),  # POST Request for User Login Authentication
]
