URL TRANSPORTE
    path('transporte/', views.transporte, name="transporte"),
    path('transporte<str:accion>', views.transporte_consultar, name="transporte_consultar"),
    path('transporte/update/<int:id>', views.update_transporte, name="update_transporte"),
    path('transporte/delete/<int:id>', views.del_transporte, name="del_transporte"),
