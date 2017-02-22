from django.conf.urls import url
from .views import  (
    comment_thread
)

urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name="thread"),
    # url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name="delete"),
]
