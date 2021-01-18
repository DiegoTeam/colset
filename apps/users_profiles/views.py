import json

from braces.views import LoginRequiredMixin
from django.conf import settings
from django.middleware.csrf import get_token
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from config.utils import convert_dict_breadcrums
from .forms import CVForm
from .models import Profile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users_profile/profile.pug'
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Mi perfil'
        kwargs['breadcrumbs'] = convert_dict_breadcrums([
            ('Inicio', reverse('index')),
            ('Perfil', '#')
        ])
        profile = None
        try:
            profile = self.request.user.profile
        except:
            kwargs["experiences"] = json.dumps([])
            kwargs["educations"] = json.dumps([])
        else:
            kwargs["experiences"] = json.dumps(profile.experience)
            kwargs["educations"] = json.dumps(profile.education)
        kwargs["profile"] = profile
        kwargs["csrf_token"] = get_token(self.request)

        return super(ProfileView, self).get_context_data(**kwargs)


class CVLoadView(LoginRequiredMixin, FormView):
    template_name = 'users_profile/cv.pug'
    login_url = settings.LOGIN_URL
    form_class = CVForm
    success_url = "../"

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Mi hoja de vida'
        kwargs['breadcrumbs'] = convert_dict_breadcrums([
            ('Inicio', reverse('index')),
            ('Perfil', '#'),
            ('Hoja de vida', '#')
        ])
        return super(CVLoadView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            profile = self.request.user.profile
        except:
            profile = Profile.objects.create(
                user=self.request.user,
                about="",
                experience=[],
                education=[]
            )

        profile.cv.save(
            form.cleaned_data["cv"].name,
            form.cleaned_data["cv"]
        )

        return super(CVLoadView, self).form_valid(form)
