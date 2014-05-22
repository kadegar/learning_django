from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$','hw.views.hello_view'),
	url(r'^$','hw.views.hello_view'),
	url(r'^about/$','hw.views.about'),
	url(r'^better/$','hw.views.better_hello')
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^hello_world/', include('hello_world.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
