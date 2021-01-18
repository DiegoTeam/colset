from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Row, Column, Submit, HTML, Button
from .models import Profile


class CVForm(forms.Form):

    cv = forms.FileField(widget=forms.FileInput(attrs={"accept": "application/pdf"}))

    def __init__(self, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(

            Row(
                Column(
                    'cv',
                    css_class='s12'
                )
            ),

            Row(
                Column(
                    Div(
                        Submit(
                            'submit',
                            'Guardar',
                            css_class='button-submit'
                        ),
                        css_class="right-align"
                    ),
                    css_class="s12"
                ),
            )
        )
