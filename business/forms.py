from django.forms import ModelForm

from .models import Empresa

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': name,
                'class': 
                ''' peer h-8 w-64 p-0 border-none bg-transparent
                    placeholder-transparent focus:border-transparent
                    focus:outline-none focus:ring-0 sm:text-sm ''',
            })