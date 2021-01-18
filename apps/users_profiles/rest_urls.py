from django.urls import path
from .rest_views import ProfileAPIView

app_name = "users_profile_api"

urlpatterns = [

    path('', ProfileAPIView.as_view(), name='profile'),

]
