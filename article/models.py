from django.db import models
#from ckeditor.fileds import RichTextField  #burada hata veriyor, burayı eklediği kısmı izle223 civarı

# Create your models here.
#uygulamaya özgü modelleri göstermemiz gerekiyor 
#bu modeller flasktakine benziyor
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name= "Yazar" )
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = models.TextField()
    #content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")    
    def __str__(self):
        return self.title#Article isimlerinin gerçek isimler olmasını sağlıyor
        #created date dersen başlık tarih olur
    class Meta:
        ordering = ['-created_date']#en son eklenen makale ilk gösteriliyor
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")#bağlantıyı kurduk
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:#yorumların sırasını sondan başa doğru sırlaıyor
        ordering = ['-comment_date']        

#////////////////////////////////////

