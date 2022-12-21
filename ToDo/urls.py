from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

]

local_urls = [

]


api_urls = [
    path('api/users/', include('apps.users.API.urls')),
]

urlpatterns += local_urls + api_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)