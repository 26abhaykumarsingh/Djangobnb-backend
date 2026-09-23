"""
URL configuration for djangobnb_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "properties": {
                "list": reverse("api_properties_list", request=request, format=format),
                "create": reverse(
                    "api_create_property", request=request, format=format
                ),
            },
            "chat": {
                "conversations": reverse(
                    "api_conversations_list", request=request, format=format
                ),
            },
            "auth": {
                "register": reverse("rest_register", request=request, format=format),
                "login": reverse("rest_login", request=request, format=format),
                "logout": reverse("rest_logout", request=request, format=format),
                "token_refresh": reverse(
                    "token_refresh", request=request, format=format
                ),
                "my_reservations": reverse(
                    "api_reservations_list", request=request, format=format
                ),
            },
        }
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api_root, name="api-root"),
    path("api/properties/", include("property.urls")),
    path("api/auth/", include("useraccount.urls")),
    path("api/chat/", include("chat.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
