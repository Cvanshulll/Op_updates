
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',head, name='he'),
    path('recipes/',recipes, name='recipes'),
    path('delete-recipe/<int:id>/',delete_recipe, name='delete_recipe'),
    path('update-recipe/<int:id>/',update_recipe, name='update_recipe'),
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
