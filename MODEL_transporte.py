MODEL TRANSPORTE

class Transporte(models.Model):
    mes = models.CharField(max_length=64, verbose_name='Mes:', default='')
    estado = models.CharField(max_length=64, verbose_name='Estado:', default='')
    transporte = models.CharField(max_length=64, verbose_name='Transporte:', default='')
    cantidad = models.CharField(max_length=64, verbose_name='Cantidad:', default='')
