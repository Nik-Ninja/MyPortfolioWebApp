
from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', blog.views.goToHomePage, name='home'),
    path('admin/', admin.site.urls),
    path('job/', include('job.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
