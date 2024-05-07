from django import forms

from remission.models import Detail

class DetailForm(forms.ModelForm):
    def setNumber():
        return f'R-{300 + Detail.objects.count()}'
    
    number = forms.CharField(label='Remision', max_length=10, required=False, initial=setNumber)
    
    class Meta:
        model = Detail
        fields = ("number","client","orders","total",)
