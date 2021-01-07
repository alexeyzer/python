from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('paterson/', views.gun1, name='paterson'),
    path('kalashnikov/', views.gun2, name='ak47'),
    path('svd/', views.gun3, name='svd'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)