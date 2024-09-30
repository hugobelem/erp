from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


from .models import Business
from .forms import BusinessForm

from static.assets import avatar


def navbar(request):
    user = request.user

    if request.user.is_authenticated:
        try:
            business = Business.objects.filter(user=user).first()
        except Business.DoesNotExist:
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
    business = Business.objects.filter(user=request.user).first()
    form = BusinessForm(instance=business)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business:empresa')
        
    context = {'form': form}
    context.update(navbar(request))
    return render(request, 'business/pages/empresa_update.html', context)