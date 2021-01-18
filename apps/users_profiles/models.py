from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User
from config.extrafields import ContentTypeRestrictedFileField


def upload_dynamic_cover(instance, filename):
    return '/'.join(['Users', 'Cover', str(instance.id), filename])


def upload_dynamic_photo(instance, filename):
    return '/'.join(['Users', 'Photo', str(instance.id), filename])


def upload_dynamic_cv(instance, filename):
    return '/'.join(['Users', 'CV', str(instance.id), filename])


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    about = models.TextField()
    cover = ContentTypeRestrictedFileField(
        upload_to=upload_dynamic_cover,
        blank=True,
        content_types=['image/jpg', 'image/jpeg', 'image/png'],
        max_upload_size=10485760
    )
    photo = ContentTypeRestrictedFileField(
        upload_to=upload_dynamic_photo,
        blank=True,
        content_types=['image/jpg', 'image/jpeg', 'image/png'],
        max_upload_size=10485760
    )
    experience = models.JSONField(default=dict, blank=True, null=True)
    education = models.JSONField(default=dict, blank=True, null=True)
    cv = ContentTypeRestrictedFileField(
        blank=True,
        upload_to=upload_dynamic_cv,
        content_types=[
            'application/pdf',
        ],
        max_upload_size=104857600
    )

    def url_cv(self):
        url = None
        try:
            url = self.cv.url
        except:
            pass
        return url
