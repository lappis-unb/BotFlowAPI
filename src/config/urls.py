from django.contrib import admin
from django.urls import path, include

from api.urls import urlpatterns

urlpatterns = [
 path('admin/', admin.site.urls),
 path('api/v1/', include(urlpatterns))
]
