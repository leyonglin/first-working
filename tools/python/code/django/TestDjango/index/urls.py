from django.conf.urls import url
from .views import *
urlpatterns = [
    # url(r'^$',index_views),
    # url(r'^login$',login_views),
    # url(r'^register$',register_views),
    # url(r'^01-temp/$',temp_views),
    # url(r'^02-var/$',var_views),
    url(r'^03-static/$',static_views),
    ]

urlpatterns += [
    # url(r'^06-add/$',add_views),
    # url(r'^07-query/$',query_views),
    # url(r'^08-update/$',update_views),
    # url(r'^09-queryall/$',queryall_views),
    # url(r'^10-delete/(\d+)/$',delete_views),
    ]

urlpatterns += [
    url(r'^11-homework/$',homework_views),
    

    ]