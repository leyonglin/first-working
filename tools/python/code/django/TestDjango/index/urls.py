from django.conf.urls import url
from .views import *
urlpatterns = [
    # url(r'^$',index_views),
    # url(r'^login$',login_views),
    # url(r'^register$',register_views),
    # url(r'^01-temp/$',temp_views),
    # url(r'^02-var/$',var_views),
    # url(r'^03-static/$',static_views),
    ]

urlpatterns += [
    # url(r'^06-add/$',add_views),
    # url(r'^07-query/$',query_views),
    # url(r'^08-update/$',update_views),
    # url(r'^09-queryall/$',queryall_views),
    # url(r'^10-delete/(\d+)/$',delete_views),
    # url(r'^11-homework/$',homework_views),
    ]

urlpatterns += [
    # url(r'^13-oto/$',oto_views),
    # url(r'^14-otm/$',otm_views),
    # url(r'15-mtm/$',mtm_views),
    ]

urlpatterns += [
    # url(r'^16-objects/$',objects_views),
    ]

urlpatterns += [
    # url(r'^01-request/$',request_views),
    # url(r'^02-request',request02_views),
    # url(r'^03-post/$',post_views),
    ]

urlpatterns += [
    #注册页面
    # url(r'^04-register/$',register_views),
    ]

urlpatterns += [
    #form模块
    # url(r'^06-form/$',form_views),
    # url(r'^08-widget1/$',widget1_views),
    # url(r'^09-widget2/$',widget2_views),
    ]

urlpatterns += [
    url(r'^12-ajax/$',ajax_views),
    url(r'^12-server/$',server12_views),
    ]