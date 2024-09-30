from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Business

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


def empresa(request):
    context = {}
    context.update(navbar(request))

    return render(request, 'business/pages/empresa.html', context)

