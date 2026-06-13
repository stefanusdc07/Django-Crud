from django.urls import path
from django.contrib import admin

# import View dari todo Application
from .views import index_view, detail_view, create_view, delete_view, CustomLoginView

app_name = 'todo'
urlpatterns = [
	# url untuk halaman daftar task
    path('', index_view, name='index'),
    # url untuk halaman detail task
    path('<int:task_id>', detail_view, name='detail'),
    # url untuk halaman tambah task
    path('create', create_view, name='create'),
    #url hapus data
    path('delete/<int:task_id>', delete_view, name='delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

