from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # add posts
    url(r'^create/$', 'blog.views.create'),
    
    # view posts
    url(r'^all/$', 'blog.views.all_post'),
    url(r'^get/(?P<blog_id>\d+)/$', 'blog.views.one_post'),
    
    #delete posts
    url(r'^delete/(?P<blog_id>\d+)/$', 'blog.views.del_post'),
    
    # login and logout urls
    url(r'^accounts/login/$', 'blog.views.login'),
    url(r'^accounts/auth/$', 'blog.views.auth_view'),
    url(r'^accounts/logout/$', 'blog.views.logout'),
    url(r'^accounts/loggedin/$', 'blog.views.loggedin'),
    url(r'^accounts/invalid/$', 'blog.views.invalid_login'),

    # register urls
    url(r'^accounts/register/$', 'blog.views.register_user'),
    url(r'^accounts/register_success/$', 'blog.views.register_success'),
    
    # search url
    url(r'^search/$', 'blog.views.search_titles'),
    
    # about url
    url(r'^about/$', 'blog.views.about'),
)