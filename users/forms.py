from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
        ]
        labels = {
            'email': 'e-mail',
            'name': 'nome'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = 'confirmar senha'

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'peer h-8 w-64 border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm',
                'autofocus': 'false',
                'placeholder': name,
            })

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'username'
        ]
        labels = {
            'email': 'e-mail',
            'name': 'nome'
        }
    

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'peer h-8 w-64 border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm',
                'autofocus': 'false',
                'placeholder': name,
            })    