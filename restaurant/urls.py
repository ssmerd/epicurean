
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls', 'auth'),
         namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('booking.urls'))
]
