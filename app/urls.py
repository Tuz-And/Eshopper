
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')),
    # path('cart', include('cart.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('products', include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
