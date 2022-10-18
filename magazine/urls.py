
from django.contrib import admin
from django.urls import path
from articles.views import about, index, detail, login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', about, name='about'),
    path('articles/<int:id>/', detail, name='retrieve'),
    path('login/', login, name='Login'),
    path('', index, name='index')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)