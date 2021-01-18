from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics, status
from .serializers import ProfileSerializer
from rest_framework.response import Response
from .models import Profile, User


class ProfileAPIView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"user": self.request.user}

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile_data = {
            "about": serializer.data.get("about"),
            "experience": serializer.data.get("experience"),
            "education": serializer.data.get("education")
        }

        user_data = {
            "first_name": serializer.data.get("first_name"),
            "last_name": serializer.data.get("last_name"),
        }

        try:
            profile = request.user.profile
        except:
            Profile.objects.create(user=request.user, **profile_data)
        else:
            Profile.objects.filter(id=profile.id).update(**profile_data)

        User.objects.filter(id=request.user.id).update(**user_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
