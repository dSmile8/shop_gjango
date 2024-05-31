from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from users.views import CustomPasswordComplete

urlpatterns = [
    path('users/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('users/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('users/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('users/reset/done/', CustomPasswordComplete.as_view(), name='password_reset_complete'),

    path("admin/", admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('bloging/', include('bloging.urls', namespace='bloging')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
