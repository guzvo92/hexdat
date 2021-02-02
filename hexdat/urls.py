
#[Global] urls.py

from django.contrib import admin
from django.urls import path, include

hash_gman = 290792
hash_denna = 12345678

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.appmain0core.urls')),
    path('mon/', include('app.appx1moneytrack.urls')),
    path(str(hash_gman)+'/', include('app.appz1gman.urls')),
    #path(str(hash_denna), include('app.appz2denna.urls')),
    path('masteradmin/', include('app.appmain1admin.urls')),
    path ('accounts/', include ('django.contrib.auth.urls')),
    path ('accounts/', include ('app.appmain1registration.urls')),
    path ('projects/', include ('app.appz0projects.urls')),

]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
