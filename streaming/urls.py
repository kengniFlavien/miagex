from django.conf.urls import url
from . import views

app_name = "streaming"

urlpatterns = [
    url(r'^$',views.stream_view,name='stream'),
    url(r'^/data/$',views.stream_data,name='streamdata'),

]