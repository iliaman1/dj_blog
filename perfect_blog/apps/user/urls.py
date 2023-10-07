from django.urls import path

from .views import Registration, Login, logout_user

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
