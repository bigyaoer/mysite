from django.urls import path
from . import views


app_name = 'lib'
urlpatterns = [
	path('',views.index,name='index'),
	path('detail/',views.detail,name='detail'),
	path('addBook/',views.addBook,name='addBook'),
	path('delBook/<int:book_id>',views.deleteBook,name='delBook'),
	path('about/',views.about,name='about'),
	path('project/',views.project,name='project'),
	path('timeless/',views.timeless,name='timeless'),
	path('spider/',views.spider,name='spider'),

	path('test/',views.test,name="test"),
]