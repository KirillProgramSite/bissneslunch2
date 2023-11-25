from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from api import views
from back_end import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu', views.MenuList.as_view(), name="menu"),
    path('api/review', views.ReviewList.as_view(), name="review"),
    path('api/basket', views.BasketList.as_view(), name="basket"),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
