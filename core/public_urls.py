from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/patient/", include("patient.urls")),
    # path("api/auth/", include("auth.urls")),
    # path("api/user/", include("user.urls")),
    # path("api/system/", include("system.urls")),
]
