from django import forms
from .models import gmud
from foundation_filefield_widget.widgets import FoundationFileInput


Clientes = [
        (1, 'Sage'),
        (2, 'Cetelem'),
        (3, 'Bradesco'),
        (4, 'Heineken'),
        (5, 'Guardian'),
        (6, 'Adtalem'),
        (7, 'Allergan'),
    ]
Criticidades = [
        (1, 'Nenhuma'),
        (2, 'Baixa'),
        (3, 'Media'),
        (4, 'Alta'),
        (5, 'Critico')
    ]
Status = [
        (1, 'Pendente'),
        (2, 'Aguardando Cliente'),
        (3, 'Aprovado'),
        (4, 'Reprovado'),
        (5, 'Finalizado'),
    ]
EndStatus = [
    (5, 'Finalizado'),
    (6, 'Rollback'),
]

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class GmudCreateForm(forms.ModelForm):
    class Meta:
        model = gmud
        fields = ['titulo', 'cliente', 'criticidade', 'resumo', 'data', 'hora', 'procedimento', 'servidores']
        widgets = {
            'data': DateInput(),
            'hora': TimeInput(),
        }
class GmudUpdateForm(forms.ModelForm):
    class Meta:
        model = gmud
        fields = ['titulo', 'cliente', 'criticidade', 'resumo', 'data', 'hora', 'procedimento', 'status', 'servidores']
        widgets = {
            'hora': TimeInput()
        }
class GmudEndForm(forms.ModelForm):
    class Meta:
        model = gmud
        fields = ['status', 'resolucao']
        def __init__(self, *args, **kwargs):
            super(GmudEndForm, self).__init__(*args, **kwargs)
            self.fields[0].choices = EndStatus