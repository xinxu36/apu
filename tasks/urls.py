from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('tasks.views',
    url(r'^$', 'index'),
    url(r'^new_task/$', 'new_task'),
    url(r'^add_task/$', 'add_task'),
)

urlpatterns += staticfiles_urlpatterns()


