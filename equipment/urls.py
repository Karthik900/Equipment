from django.contrib import admin
from django.urls import path, include

# app_name = 'details'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equip/', include('details.urls'))
]
