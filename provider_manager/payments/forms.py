from django import forms
from payments.models import Provider



class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = ("user","bill","value","description","createdAt")


