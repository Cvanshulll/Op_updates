
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',head, name='he'),
    path('opportunities/',opportunities, name='opportunities'),
    path('delete-opportunity/<int:id>/',delete_opportunity, name='delete_opportunity'),
    path('update-opportunity/<int:id>/',update_opportunity, name='update_opportunity'),
    path('add-opportunity/',add_opportunity, name='add_opportunity'),
    path('about/',about, name='about'),
    path('login/',login_page, name='login'),
    path('logout/',logout_page, name='logout'),
    path('contact/',contact, name='contact'),
    path('register/',register_page, name='register'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)