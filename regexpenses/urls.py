from django.urls import path

from . import views

app_name = 'regexpenses'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.add_data, name='nodata'),
    path('<int:reg_id>/', views.detail, name='detail'),
    path('iptamt/', views.input_tamt, name='iptamt'),
    path('delete/<int:rid>', views.del_itm, name='delete_itm'),
]

