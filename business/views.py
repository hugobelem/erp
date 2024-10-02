from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


from .models import Empresa
from .forms import EmpresaForm

from static.assets import avatar


def navbar(request):
    user = request.user

    if request.user.is_authenticated:
        try:
            business = Empresa.objects.filter(user=user).first()
        except Empresa.DoesNotExist:
            business = None

        svg = avatar.generate(request.user.name)
        first_name = request.user.name.split()[0]

        context = {
            'first_name': first_name,
            'avatar': mark_safe(svg),
            'business': business
        }
    
    return context


@login_required(login_url='login')
def empresa(request):
    context = {}
    context.update(navbar(request))

    return render(request, 'business/pages/empresa.html', context)


@login_required(login_url='login')
def empresa_update(request):
    business = Empresa.objects.filter(user=request.user).first()

    form = EmpresaForm(instance=business)

    if request.method == 'POST':
        if not business:
            form = EmpresaForm(request.POST, request.FILES)
            if form.is_valid():
                business = form.save()
                user = request.user
                user.business = business
                user.save()
        else:
            form = EmpresaForm(request.POST, request.FILES, instance=business)
            if form.is_valid():
                form.save()
                return redirect('business:empresa')
        
    context = {'form': form}
    context.update(navbar(request))
    return render(request, 'business/pages/empresa_update.html', context)