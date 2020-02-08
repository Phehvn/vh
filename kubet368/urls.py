"""kubet368 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index top"),
    path('the-thao/', views.thethao, name="the thao"),
    path('the-thao/<str:slug>/<int:id>', views.thethaolist, name="danh sach bai viet"),
    path('the-thao/<str:art_slug>.html&id=<int:art_id>', views.thethaodetail, name="bai viet"),
    path('xo-so/', views.xoso, name="xổ số"),
    path('xo-so/<str:slug>/<int:id>', views.xosolist, name="danh sach bai viet"),
    path('xo-so/<str:art_slug>.html&id=<int:art_id>', views.thethaodetail, name="bài viết xổ sô"),
    path('xo-so/xo-so-online.html', views.xosoonline, name="kết quả xổ số 3 miền"),
    path('xo-so/xo-mo.html', views.xomo, name="xổ mơ"),
    path('<str:slug>/<int:id>', views.thethaolist, name="games"),
    path('ban-ca.html', views.banca, name="games bắn cá"),

    path('huong-dan/', views.huongdan, name="hướng dẫn"),
    path('huong-dan/<str:art_slug>.html&id=<int:art_id>', views.huongdanarticle, name="bài viết hướng dẫn"),
    path('kinh-nghiem/', views.kinhnghiem, name="kinh nghiệm"),
    path('kinh-nghiem/<str:art_slug>.html&id=<int:art_id>', views.kinhnghiemarticle, name="bài viết hướng dẫn"),
    path('khuyen-mai/', views.uudai, name="kubet ưu đãi"),
    path('khuyen-mai/<str:art_slug>.html&id=<int:art_id>', views.huongdanarticle, name="bài viết hướng dẫn"),
    path('anh-nong-18/<str:art_slug>.html&id=<int:art_id>', views.huongdanarticle, name="bài viết ảnh nóng"),
    path('ku-casino.html', views.kucasino, name="ku casino"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)