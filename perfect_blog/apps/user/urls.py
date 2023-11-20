from django.urls import path

from .views import Registration, Login, logout_user, ShowProfile, EditProfile

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<str:name>', ShowProfile.as_view(), name='showprofile'),
    path('editprofile/<str:name>', EditProfile.as_view(), name='editprofile'),
]
