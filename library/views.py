from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from django.urls import reverse
# Create your views here.
# 主页
def index(request):
	return render(request,"home/index.html")
# 关于
def about(request):
	return render(request,"home/about.html")
# 项目详情
def project(request):
	return render(request,"home/work.html")
# 爬虫使用一种模板
def spider(request):
	return render(request,"spider.html")
# django、appium、笔记使用文章类模板
def django(request):
	return render(request,"home/article.html")
# 时间轴模板
def timeless(request):
	return render(request,"timeless/timeline2.html")

def test(request):
	return render(request,"test.html")






def detail(request):
	book_list = Book.objects.order_by('-pub_date')[:5]
	context = {'book_list':book_list}
	return render(request,'lib/detail.html',context)

def addBook(request):
	if request.method == 'POST':
		temp_name = request.POST['name']
		temp_author = request.POST['author']
		temp_pub_house = request.POST['pub_house']

	from django.utils import timezone
	temp_book = Book(name=temp_name,author=temp_author,pub_house=temp_pub_house,pub_date=timezone.now())
	temp_book.save()

	return HttpResponseRedirect(reverse('lib:detail'))

def deleteBook(request,book_id):
	bookId = book_id
	Book.objects.filter(id=bookId).delete()
	return HttpResponseRedirect(reverse('lib:detail'))

# def page_not_found(request):
# 	from django.shortcuts import render_to_response
# 	response = render_to_response('404.html')
# 	response.status_code = 404
# 	return response
	