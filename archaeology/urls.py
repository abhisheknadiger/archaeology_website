"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
app_name = 'archaeology'




#normal url patterns
urlpatterns = [
	url(r'^$' , views.home ,name= 'home'),
	url(r'^search$',views.search, name = 'search'),
	url(r'^contact_us$',views.contact, name = 'contact'),
	url(r'^missions/$', views.mission, name = 'mission'),
]
#urls for publications

urlpatterns = urlpatterns + [
	url(r'^good_feedback$',views.good_feedback,name='good_feedback'),
]

urlpatterns = urlpatterns + [

	url(r'^publication/$',views.publications,name = 'publication'),
	url(r'^add_publication/$',views.add_publication , name='add_publication'),
	url(r'^delete_publication/(?P<publication_id>[0-9]+)$',views.delete_publicaton,name='delete_publication'),
	url(r'^view_publication/(?P<publication_id>[0-9]+)$',views.view_publication,name = 'view_publication'),
	url(r'^detail_publication/(?P<publication_id>[0-9]+)$',views.view_detailed_publication,name='detail_publication'),
	url(r'^user_view$',views.user_view,name='user_view'),
	url(r'^user_publication/$',views.user_publication,name='user_publication'),
]

#url patterns for users
urlpatterns = urlpatterns + [
	url(r'^register/$', views.register, name='register'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url (r'^user/$',views.user_details ,name='user_details'),
	url(r'^upgrade/$',views.upgrade,name='upgrade'),
]

# url pattern for monuments
urlpatterns  =urlpatterns + [
	url(r'^monument/$', views.monument_all, name = 'monument'),
	url(r'^monument/(?P<monument_id>[0-9]+)$', views.monument_details, name = 'monument_details'),
	url(r'^(?P<monument_id>[0-9]+)/add_feedback/monument/$',views.create_feedback, name = "add_feedback"),
	url(r'^download/(?P<ticket_id>[0-9]+)$', views.download_ticket, name='ticket'),
	url(r'^ticket/(?P<monument_id>[0-9]+)$', views.buy_ticket, name='monument_ticket'),
	url(r'^add_monument$',views.add_monument,name = 'add_monument'),
	url(r'^delete/monument$',views.ddelete_monument, name = "ddelete_monument"),
	url(r'^delete/monument/(?P<monument_id>[0-9]+)$',views.delete_monument, name = "delete_monument"),
	url(r'^delete/monument_feedback/(?P<feedback_id>[0-9]+)$',views.delete_feedback, name = "delete_monument_feedback"),
]
#url pattern for excavation
urlpatterns  =urlpatterns + [
	url(r'^excavation/$', views.excavation_all, name = 'excavation'),
	url(r'^excavation/(?P<excavation_id>[0-9]+)$', views.excavation_details, name = 'excavation_details'),
	url(r'^buy_excavation_ticket/(?P<excavation_id>[0-9]+)$',views.buy_excavation_ticket,name="excavation_ticket"),
	url(r'^excavation/ticket/(?P<excavation_id>[0-9]+)$', views.download_excavation_ticket, name='excavation_ticket_download'),
	url(r'^add_excavation$', views.add_excavation, name='add_excavation'),
	url(r'^delete/excavation$',views.ddelete_excavation, name = "ddelete_excavation"),
	url(r'^delete/excavation/(?P<publication_id>[0-9]+)$',views.delete_excavation, name = "delete_excavation"),
]
#url pattern for Library
urlpatterns  =urlpatterns + [
	url(r'^Library/$', views.Library_all, name = 'Library'),
	url(r'^Library/(?P<Library_id>[0-9]+)$', views.Library_details, name = 'Library_details'),
	url(r'^add_library$',views.add_library,name='add_library'),
	url(r'^delete/library$',views.ddelete_library, name = "ddelete_library"),
	url(r'^delete/library/(?P<publication_id>[0-9]+)$',views.delete_library, name = "delete_library"),
]



#url pattern for Artifact
urlpatterns  =urlpatterns + [
	url(r'^artifact/$', views.artifact_all, name = 'artifact'),
	url(r'^artifact/(?P<artifact_id>[0-9]+)$', views.artifact_details, name='artifact_details'),
	url(r'^(?P<artifact_id>[0-9]+)/add_feedback/artifact/$',views.create_artifact_feedback, name = "add_artifact_feedback"),
	url(r'^add_artifact$',views.add_artifact,name = 'add_artifact'),
	url(r'^delete/artifact$',views.ddelete_artifact, name = "ddelete_artifact"),
	url(r'^delete/artifact/(?P<publication_id>[0-9]+)$',views.delete_artifact, name = "delete_artifact"),
	url(r'^delete/artifact_feedback/(?P<feedback_id>[0-9]+)$',views.delete_artifact_feedback, name = "delete_artifact_feedback"),
]

#url pattern for Musuem
urlpatterns =  urlpatterns + [
	url(r'^musuem/$', views.musuem_all, name = 'museum'),
	url(r'^musuem/(?P<musuem_id>[0-9]+)$', views.musuem_details, name='museum_details'),
	url(r'^add_museum$',views.add_museum,name = 'add_museum'),
	url(r'^add_feedback/musuem/(?P<museum_id>[0-9]+)$',views.create_museum_feedback, name = "add_museum_feedback"),
	url(r'^buy_museum_ticket/(?P<museum_id>[0-9]+)$',views.buy_museum_ticket,name="museum_ticket"),
	url(r'^museum/ticket/(?P<ticket_id>[0-9]+)$', views.download_museum_ticket, name='museum_ticket_download'),
	url(r'^delete_museum/(?P<museum_id>[0-9]+)$',views.delete_museum, name = 'delete_museum'),
	url(r'^delete/museum$',views.ddelete_museum, name = "ddelete_museum"),
	url(r'^delete/museum/(?P<publication_id>[0-9]+)$',views.delete_museum, name = "delete_museum"),
	url(r'^delete/museum_feedback/(?P<feedback_id>[0-9]+)$',views.delete_museum_feedback, name = "delete_museum_feedback"),

]



#url pattern for project display

urlpatterns = urlpatterns + [
	url(r'add_project/$',views.add_project , name = 'add_project'),
	url(r'project/$',views.project , name = 'project'),
	url(r'^delete/project$',views.ddelete_project, name = "ddelete_project"),
	url(r'^delete/project/(?P<publication_id>[0-9]+)$',views.delete_project, name = "delete_project"),
]

