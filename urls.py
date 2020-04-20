from django.urls import path

import views

urlpatterns = [
    path('', views.homepage),
    path('projects', views.projects),
    path('about-me', views.about),
    path('blog', views.blog),
]

# Boilerplate to include static files.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static('static/', document_root=settings.STATIC_ROOT)

