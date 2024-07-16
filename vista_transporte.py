VISTAS TRANSPORTE

# VISTAS DE PLANIFICACION -  TRANSPORTE
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def transporte(request):
    if request.method == 'POST':
        form21 = TransporteForm(request.POST)
        if form21.is_valid():
            form21.save()
            return redirect("/planificacion/transporte#success")
        else:
            context = {'form21': form21}
            return render(request, 'transporte.html', context)
    transportee =  Transporte.objects.all()
    paginator = Paginator(transportee, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form21': TransporteForm(), 'formtras': TransporteEForm(), 'transportee': pagina_actual}
    return render(request, 'transporte.html', context)

# VISTAS DE ACTUALIZACIÓN DE PLANIFICACION - TRANSPORTE
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'superusuario'])
def update_transporte(request, id):
    queryset = Transporte.objects.get(id=id)
    form21 = TransporteForm(instance=queryset)
    if request.method == 'POST':
        form21 = TransporteEForm(request.POST, instance=queryset)
        if form21.is_valid():
            form21.save()
            return redirect('/transporte#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PLANIFICACION - TRANSPORTE
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'superusuario'])
def del_transporte(request, id):
    if request.method == 'POST':
        form = Transporte.objects.get(id=id)
        form.delete()
        return redirect('/transporte#deletesuccess')

# VISTAS DE CONSULTAR DE PLANIFICACION - TRANSPORTE
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def transporte_consultar(request, accion):
    if accion == 'consultar':
        if 'name' in request.GET:
            estado = request.GET['estado']
            transportee = Transporte.objects.filter(estado__contains=estado).values()
            paginator = Paginator(transportee, 15) # 15 objetos por página
            pagina = request.GET.get('page')
            try:
                # Obtener la página solicitada
                pagina_actual = paginator.page(pagina)
            except PageNotAnInteger:
                # Si la página no es un entero, redirigir a la primera página
                pagina_actual = paginator.page(1)
            except EmptyPage:
                # Si la página está fuera de rango, redirigir a la última página
                pagina_actual = paginator.page(paginator.num_pages)
    context = {'form21': TransporteForm(), 'formtras': TransporteEForm(), 'transportee': pagina_actual}
    return render(request, 'transporte.html', context)
