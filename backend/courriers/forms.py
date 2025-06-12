from django import forms
from .models import Courrier

class CourrierForm(forms.ModelForm):
    class Meta:
        model = Courrier
        fields = "__all__"  # Or list only the fields you want to expose
