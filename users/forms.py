from django  import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#modificando el perfil
from .models import Profile


#Creando otros campos para el fomulario
# Registration hereda de Creation: username, pass1 y pass2, el correo es adicional se está personalizando
class UserRegisterForm(UserCreationForm):
    #por default, required = True
    email = forms.EmailField()
    
    class Meta:
        # para crear un nueo user
        model = User
        #campos y el orden en q se mostraran en el form
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        # para crear un nueo user
        model = User
        #campos y el orden en q se mostraran en el form
        fields = ['username', 'email']

#para actualiza foto        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['image']
    
    
    

