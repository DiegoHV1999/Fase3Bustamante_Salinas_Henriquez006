from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('sobrenosotros/', views.sobrenosotros, name='sobrenosotros'),
    path('local/<int:pk>/', views.LocalDetailView.as_view(), name='local_detail'),
    path('local/', views.LocalListView.as_view(), name='locales'),
    


]

urlpatterns+=[
    path('local/create/', views.LocalCreate.as_view(), name='local_create'),
    path('local/<int:pk>/update/', views.LocalUpdate.as_view(), name='local_update'),
    path('local/<int:pk>/delete/', views.LocalDelete.as_view(), name='local_delete'),
    
    
]