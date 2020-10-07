from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.news_of_day,name='news_of_day'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
]

