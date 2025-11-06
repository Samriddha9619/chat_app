from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing_page.html'), name='landing'),
    path('chat/', TemplateView.as_view(template_name='index.html'), name='chat'),
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')