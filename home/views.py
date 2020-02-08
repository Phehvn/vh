from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from home.models import Category,Article
# Create your views here.
def index(request):
    return render(request, 'home/index.html')
    #return HttpResponse("trang chu")
def thethao(request):
    listBlogs = Article.objects.filter(cat_id__in = [1,3,4])
    return render(request, 'the-thao/index.html',{'blogs':listBlogs})
def thethaolist(request, slug, id):
    categories = Category.objects.get(slug = slug)
    danhsach = Article.objects.filter(cat_id = id)
    catename = Category.objects.filter(cat_id = id)
    return render(request, 'the-thao/danh-muc-bai-viet.html', {'categoriesname':catename,'listarticle':danhsach})
def thethaodetail(request, art_slug, art_id):
    danhsach = Article.objects.filter(art_id = art_id)
    return render(request, 'the-thao/bai-viet.html', {'listarticle':danhsach})
def xoso(request):
    listBlogs = Article.objects.filter(cat_id__in = [2,5,6])
    return render(request, 'xo-so/index.html', {'blogs':listBlogs})
def xosolist(request, slug, id):
    categories = Category.objects.get(slug = slug)
    danhsach = Article.objects.filter(cat_id = id)
    catename = Category.objects.filter(cat_id = id)
    return render(request, 'xo-so/danh-muc-bai-viet.html', {'categoriesname':catename,'listarticle':danhsach})
def xosoonline (request):
    return render(request, 'xo-so/xo-so-online.html')
def xomo (request):
    return render(request, 'xo-so/xo-mo.html')
def banca (request):
    return render(request, 'home/ban-ca.html')
def huongdan(request):
    listBlogs = Article.objects.filter(cat_id__in = [7])
    return render(request, 'huong-dan/index.html', {'blogs':listBlogs})
def huongdanarticle(request,art_slug, art_id):
    listBlogs = Article.objects.filter(art_id = art_id)
    return render(request, 'huong-dan/bai-viet.html', {'blogs':listBlogs})
def kinhnghiem(request):
    listBlogs = Article.objects.filter(cat_id__in = [13,14,15,16,17])
    return render(request, 'kinh-nghiem/index.html', {'blogs':listBlogs})
def kinhnghiemarticle(request,art_slug, art_id):
    listBlogs = Article.objects.filter(art_id = art_id)
    return render(request, 'kinh-nghiem/bai-viet.html', {'blogs':listBlogs})
# cac bai viet khac
def kucasino(request):
    return render(request, 'home/ku-casino.html')
def uudai(request):
    danhsach = Article.objects.filter(cat_id__in = [11])
    return render(request, 'home/khuyen-mai-nha-cai-kubet.html', {'listarticle': danhsach})
