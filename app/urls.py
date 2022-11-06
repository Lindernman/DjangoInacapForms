from django.shortcuts import render

# Create your views here.


from django.urls import include, path


from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('personas', views.PersonasView.as_view(), name='personas'),
    path('personas/registrar', views.registrar, name='registrar'),
    path('personas/<pk>', views.DetalleView.as_view(), name='detalle'),
    path('personas/<id>/eliminar', views.eliminar, name='eliminar'),
    path('personas/<int:id>/actualizar', views.actualizar, name='actualizar'),

]


#
