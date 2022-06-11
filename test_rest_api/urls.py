"""test_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from jobs_app.views import EndJobApi, JobApiList
from nft_shop_app.views import NftApiList, NftBuyApi
from users_app.views import LevelUpdateApiView

schema_view = get_schema_view(
    openapi.Info(
        title='test',
        default_version='v1',
        description='desc',
    ),
    public=False,
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),

    path(r'auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),

    path('api/v1/nft_list/', NftApiList.as_view()),
    path('api/v1/nft_buy/', NftBuyApi.as_view()),
    path('api/v1/jobs/', JobApiList.as_view()),
    path('api/v1/end_job/', EndJobApi.as_view()),
    path('api/v1/up_productivity/', LevelUpdateApiView.as_view())
]
