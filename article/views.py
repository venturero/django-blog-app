from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm 
from .models import Article,Comment
from django.apps import apps 
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#/detail/7 dersen Detail:7
# Create your views here.
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})
def index(request):
    return render(request,"index.html")
#django gidiyor templates klasörüne bakıyor  

def about(request):   
    return render(request,"about.html")
def detail(request,id):
    return HttpResponse("Detail:" + str(id))
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)#yazar bilgisini belirtmeden makaleyi oluşturmaya çalışırsan django hata verir
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

    return render(request,"update.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)#yazar bilgisini belirtmeden makaleyi oluşturmaya çalışırsan django hata verir
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard")
@login_required(login_url = "user:login")
def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        #comment şeklinde obje oluşturuyoruz
        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))#dinamic olması için reverse olması lazım
#id yi vermek için kwargs kullanıyoruz










    