from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', include('mainpage.urls')),
    path('common/', include('common.urls')),
    path('regexpenses/', include('regexpenses.urls')),

]