#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Div, HTML


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': "form-control form-control-lg inverse-mode"})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña', 'class': "form-control form-control-lg inverse-mode"})
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                'email',
                css_class="form-group m-b-20"
            ),
            Div(
                'password',
                css_class="form-group m-b-20"
            ),
            Div(
                ButtonHolder(
                    Submit('submit', 'Ingresar', css_class='btn btn-primary btn-block btn-lg')
                ),
                css_class="login-buttons"
            ),
            Div(
                HTML(
                    """
                    <p class="text-center" style="margin-bottom:30px;margin-top:30px;">Tambien puedes ingresar usando tus redes sociales</p>
                    <a href="{% url "social:begin" "facebook" %}" class="btn btn-social btn-block btn-lg btn-facebook text-center">
                        <span class="fab fa-facebook-f"></span> Ingresar con Facebook
                    </a>
                    <a href="{% url "social:begin" "google-oauth2" %}" class="btn btn-social btn-block btn-lg btn-google text-center">
                        <span class="fab fa-google"></span> Ingresar con Google
                    </a>
                    """
                )
            )
        )
