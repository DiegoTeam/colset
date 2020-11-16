from urllib.parse import urlencode, urlparse, urlunparse, parse_qs
from social_core.backends.facebook import FacebookOAuth2
from social_core.backends.google import GoogleOAuth2
from social_core.backends.twitter import TwitterOAuth
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from urllib.request import urlopen


def save_profile_picture(backend, user, response, details, is_new=False, *args, **kwargs):

    user.is_verificated = True
    user.save()

    if isinstance(backend, FacebookOAuth2):
        url = 'http://graph.facebook.com/{0}/picture?width=1000'.format(response['id'])
        avatar = urlopen(url)
        user.photo.save(slugify(str(user.id)) + '.jpg',
                            ContentFile(avatar.read()))
        user.save()

    if isinstance(backend, TwitterOAuth):
        if response.get('profile_image_url'):
            url = response.get('profile_image_url').replace('_normal','')
            avatar = urlopen(url)
            user.photo.save(slugify(str(user.id)) + '.jpg',
                            ContentFile(avatar.read()))
            user.save()

    if isinstance(backend, GoogleOAuth2):
        if response.get('picture'):
            url = response.get('picture')
            avatar = urlopen(url)
            user.photo.save(slugify(str(user.id)) + '.jpg',
                            ContentFile(avatar.read()))
            user.save()
