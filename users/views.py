from django.shortcuts import render, redirect
#Para la creacion de formularios - usuario y contraseña, COMO SE USA META, se quita
# from django.contrib.auth.forms import UserCreationForm
# crear mensajes flash
from django.contrib import messages

from django.contrib.auth.decorators import login_required

#Una vez creado en forms.py el correo mediante la clase Meta
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm #actualizdr


# Create your views here.

def register(request):
    #validaciones del metodo
    if request.method == 'POST':
        
        # form = UserCreationForm(request.POST) renombrando cuando ya se ha creado la clase con Meta
        form = UserRegisterForm(request.POST)
        
        #validacion del formulario
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created, you can login!')
            #hacer eso y luego redirect (importar), esto se vincula al base.html para q los mensajes aparezca en cualquie pagina como message.tags
            return redirect('login')
    else:
        #si no hay post request, solo se crea al formulario vacio
        # form = UserCreationForm()
        #Reemplazando lo creado con META
        form = UserRegisterForm()
        
    return render(request, 'users/register.html',{'form': form})

#Para restringir paginas sin login
@login_required
def profile(request):
    #update info y fotografia
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    # si no se quiere actualizar, solo se extraen los campos al form
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
    context = {
        'u_form':u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

    

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

