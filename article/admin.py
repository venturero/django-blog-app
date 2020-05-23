#set_password diye verirsen o zaman şifrelenir, yoksa şifrelenmez
#Article.objects.create bütün işlemleri kendi yapıyor
from django.contrib import admin

from .models import Article,Comment
# Register your models here.
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):#class içinde class yazıyoruz
    
    list_display = ["title","author","created_date","content"]#bundaki content hocanınkinde yok

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]#içine title da yazabilirsin

    class Meta:#django tarafından söylenen class, o yüzden bu isim lazım
        model = Article

#////////////////////////////


# Register your models here.




