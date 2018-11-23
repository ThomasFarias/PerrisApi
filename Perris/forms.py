from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe          
from .models import Cliente,Rescatado


class FormRegistroCliente(forms.ModelForm):
	run =forms.CharField(widget=forms.TextInput(),label="RUN")
	password2 =forms.CharField(widget=forms.PasswordInput(),label="Confirmar contraseña")
	fono_numero =forms.CharField(widget=forms.TextInput(),label="Telefono",required=False)

	class Meta:
		model = User
		# specify what fields should be used in this form.
		fields = ('email',
				'username', 'password','first_name','last_name','password2',
				)


	def __init__(self, *args, submit_title="Enviar", **kwargs):
		super().__init__(*args, **kwargs)
		#user = super().save(commit=False) #snippet
		self.helper=FormHelper()
		self.fields['username'].label = 'Nombre de usuario'
		self.fields['username'].help_text = None
		self.fields['password'].label = 'Contraseña'
		self.fields['password'].widget = forms.PasswordInput()
		self.fields['first_name'].label = 'Nombre'
		self.fields['email'].label = 'Correo electrónico'
		self.fields['last_name'].label = 'Apellido'
		#user.is_regular = True #snippet de como tuvo que haber sido aca
							#para autirozaciones reales, no lo pude hacer
							#porque ya usamos otra metodologia y no pueden
							#ser mezcladas



		self.helper.layout = Layout(
			Div(
				Div('run', css_class="col-sm-6"),
				Div('fono_numero', css_class="col-sm-6"),
				css_class = 'row'
			),
			Div(
				Div('username', css_class="col-sm-6"),
				Div('email', css_class="col-sm-6"),
				css_class = 'row'
			),
			Div(
				Div('first_name', css_class="col-sm-6"),
				Div('last_name', css_class="col-sm-6"),
				css_class = 'row'
			),
			Div(
				Div('password', css_class="col-sm-6"),
				Div('password2', css_class="col-sm-6"),
				css_class = 'row'
			),
			ButtonHolder(
						Submit('save', 'Enviar')
			)
		)
       


class FormRescatado(forms.ModelForm):

    class Meta:
        model = Rescatado
        fields = ('nombre',
                  'raza','descripcion','estado','foto'
                 )
    
    def __init__(self, *args, submit_title="Enviar", **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.fields['nombre'].label = 'Nombre de rescatado'
        self.fields['raza'].label = 'Raza'
        self.fields['descripcion'].label = 'Descripción'
        self.fields['estado'].label = 'Estado'

        self.helper.layout = Layout(
            Div(
                Div('nombre', css_class="col-sm-6"),
                Div('raza', css_class="col-sm-6"),
                css_class = 'row'
            ),
            Div(
                Div('descripcion', css_class="col-sm-6"),
                Div('estado', css_class="col-sm-6"),
                css_class = 'row'
            ),
            Div(
                Div('foto', css_class="col-sm-6"),
                css_class = 'row'
            ),
            ButtonHolder(
                        Submit('save', 'Aceptar')
            ),
            Div(
        ),
        )



class FormAdopcion(forms.Form):
	run=forms.CharField(widget=forms.TextInput(),required=True)
	codigo=forms.CharField(widget=forms.TextInput(),required=True)

class FormLogin(forms.Form):
	username=forms.CharField(widget=forms.TextInput(),label="Nombre de usuario")
	password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
	def __init__(self, *args, **kwargs):
		super(FormLogin, self).__init__(*args, **kwargs)
		self.fields['password'].help_text = help_text=mark_safe("<a href= \"password_reset\" >¿Olvidó su contraseña?</a>.") 
		self.helper=FormHelper()
		self.helper.layout = Layout(
			Div(
				Div('username', css_class="col-sm-10"),
				css_class = 'row'
			),
			Div(
				Div('password', css_class="col-sm-10"),
				css_class = 'row'
			),
			ButtonHolder(
                Submit('submit', 'Enviar', css_class='button white',width= 25),
                css_class = 'centrado'
            )
		)