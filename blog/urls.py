"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#url adreslerini verdiğinde çalıştırışacak kodları verir
#tüm url maplerini buraya yazıyoruz
#yeni user oluşturmak için startapp kullan
from django.contrib import admin
from django.urls import path,include
from article.views import index
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),#her url adresi fonksiyon çalıştırıyor. Bu da çalıştırılacak kodları gösteriyor
    path('', views.index,name= "index"),#boş yaptık ki localhost8000 de direk buraya yazacağım fonk çalışsın
    path('about/',views.about,name= "about"),
    path('detail/<int:id>',views.detail,name= "detail"),    
    path('articles/',include("article.urls")),#articles patternini gördükten sonra articles.url ye bak demek bu
    path('user/',include("user.urls")),
#bu şekilde uygulama ile ana dizindeki url yi bağlamış oluyoruz
#articles/ slashi unutursan olmaz
#projeyi modüler hale getiriyor, daha fazla url adresinin yazılmamasını sağlıyor
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
