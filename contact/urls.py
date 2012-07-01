from django.conf.urls import patterns, url

urlpatterns = patterns('contact.views',
    url(r'^$', 'contact'),
    url(r'^thanks/$', 'thanks')
)


