FORM TRANSPORTE

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte        
        fields = ('estado', 'mes', 'transporte', 'cantidad')
        
class TransporteEForm(forms.ModelForm):
    class Meta:
        model = Transporte        
        fields = ('estado', 'mes', 'transporte', 'cantidad')
