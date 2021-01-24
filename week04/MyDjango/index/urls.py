from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')


urlpatterns = [
    path('', views.index),
    path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),
    # 正则匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    # 自定义过滤器
    path('<myint:year>', views.year),

    # 添加数据
    path('add.html', views.add_books),

    # 查询子良
    path('books.html', views.books),

]