from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Cliente

class UsuarioForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control shadow'
        })
    )
    
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirmar Contraseña',
            'class': 'form-control shadow'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''  # esto elimina todas las etiquetas

    class Meta:
        model = Usuario
        fields = ['email', 'nom_usua', 'apell_usua', 'tele_usua']
        labels = {
            'email': 'Correo Electrónico',
            'nom_usua': 'Nombre',
            'apell_usua': 'Apellido',
            'tele_usua': 'Teléfono',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electrónico', 'class': 'form-control shadow'}),
            'nom_usua': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control shadow'}),
            'apell_usua': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control shadow'}),
            'tele_usua': forms.TextInput(attrs={'placeholder': 'Teléfono', 'class': 'form-control shadow'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # La validación de contraseñas ya la hace UserCreationForm automáticamente
        return cleaned_data
    
    
    
class CargarDatosForm(forms.Form):
    TIPOS_ARCHIVO = (
        ('csv', 'CSV'),
        ('excel', 'Excel'),
        ('json', 'JSON'),
    )
    
    tipo_archivo = forms.ChoiceField(
        choices=TIPOS_ARCHIVO,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    archivo = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.csv,.xlsx,.json'
        })
    )
    
    descripcion = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Descripción opcional del archivo...'
        })
    )
    
class PerfilForm(forms.ModelForm):
    nom_usua = forms.CharField(label="Nombre", max_length=15)
    tele_usua = forms.CharField(label="Teléfono", max_length=15)

    class Meta:
        model = Cliente
        fields = ['direc_cliente', 'nom_usua', 'tele_usua']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['nom_usua'].initial = user.nom_usua
            self.fields['tele_usua'].initial = user.tele_usua
            self.fields['direc_cliente'].initial = user.cliente.direc_cliente

    def save(self, commit=True):
        cliente = super().save(commit=False)
        user = self.instance.cod_usua

        user.nom_usua = self.cleaned_data['nom_usua']
        user.tele_usua = self.cleaned_data['tele_usua']
        if commit:
            user.save()
            cliente.cod_usua = user
            cliente.save()
        return cliente