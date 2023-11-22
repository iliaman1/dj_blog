from django.urls import path

from .views import Registration, Login, logout_user, ShowProfile, EditProfile, ShowUserPosts, ShowUserComments, \
    ShowUserVotes, ProfileFollowing

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<str:name>', ShowProfile.as_view(), name='showprofile'),
    path('profile/<str:name>/posts', ShowUserPosts.as_view(), name='showuserposts'),
    path('profile/<str:name>/comments', ShowUserComments.as_view(), name='showusercomments'),
    path('profile/<str:name>/votes', ShowUserVotes.as_view(), name='showuservotes'),
    path('profile/<str:name>/follow', ProfileFollowing.as_view(), name='followbyprofile'),
    path('editprofile/<str:name>', EditProfile.as_view(), name='editprofile'),
]
