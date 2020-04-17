from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import include
from django.urls import path
from django.conf import settings

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls')),
    path('', views.index, name='index'),
    path("login/", auth.LoginView.as_view(), name='login'),
    path("logout/", auth.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path("reset-password/", auth.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_reset'),
    path("reset-password_done/",
         auth.PasswordChangeDoneView.as_view(template_name='registration/reset-password-done.html'),
         name='password_change_done'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

