from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import SignUpView, CustomLoginView, CustomHomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', CustomHomeView.as_view(), name='home'),
    path('login/', LogoutView.as_view(next_page='login'), name='logout'),]
