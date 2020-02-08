"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from skillreader import views
# from django.conf.urls import url, include

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     #url(r'^$', views.index, name='index'),
#     #url(r'^skillreader/', include('skillreader.urls')),
#     #url(r'^$', views.upload_doc, name="upload_doc"),
#     url(r'^$', views.home, name="home"),
#     url(r'upload/', views.upload, name="upload"),

# ]

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from skillreader import views

# urlpatterns = [
#     # url(r'^$', views.index_redirect, name='index_redirect'),
#     path('admin/', admin.site.urls),
#     path('', include('skillreader.urls')),
# ]
urlpatterns = [
    url(r'^$', views.index_redirect, name='index_redirect'),
    path('admin/', admin.site.urls),
    url(r'^skillreader/', include('skillreader.urls')),  #8000/skillreader/
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
