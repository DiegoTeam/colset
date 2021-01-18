from django.urls import path, include
from .views import ProfileView, CVLoadView

app_name = 'users_profile'

urlpatterns = [

    path('', ProfileView.as_view(), name='profile'),
    path('cv/', CVLoadView.as_view(), name='cv'),
    path('api/v1.0/', include('apps.users_profiles.rest_urls', namespace="users_profile_api")),

]
