from django import forms
from django.core import validators 

class FormArticulo(forms.Form):
    title = forms.CharField(
        label='Titulo',
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.MaxLengthValidator(40, 'El titulo muy largo' ),
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'El título está mal escrito', 'invalid_title'),

        ]
    )

    content = forms.CharField(
        label='Contenido',
        max_length=40,
        required=False,
        widget=forms.Textarea(
            attrs= {
                'placeholder': 'Ingrese el contenido',
                'class': 'contenido_form_article'
            }
        )
    )

    public_options= [(1,'Si'),(0,'No')]
    public = forms.TypedChoiceField(
        label='¿Publicado?',
        choices=public_options
    )