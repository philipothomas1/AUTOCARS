from django.urls import path
from . import views
from .views import(
	car_detail,
	spare_detail,
    # SearchResultsView
)
	



app_name='cars'
urlpatterns = [
    path('', views.home,name='home'),
    path('car_detail/<slug:slug>/',views.car_detail, name='car_detail'),
    # path('car_detail/<slug>/',car_detail.as_view(),name='car_detail'),
    path('spare_detail/<slug:slug>/',views.spare_detail,name='spare_detail'),
    path('toyotacars/',views.toyotacars,name='toyotacars'),
    path('nissancars/',views.nissancars,name='nissancars'),
    path('fordcars/',views.fordcars,name='fordcars'),
    # path('toyotacars/',views.toyotacars,name='toyotacars'),
    path('bmwcars/',views.bmwcars,name='bmwcars'),
    path('audicars/',views.audicars,name='audicars'),
    path('jeepcars/',views.jeepcars,name='jeepcars'),
    path('hondacars/',views.hondacars,name='hondacars'),
    path('suzukicars/',views.suzukicars,name='suzukicars'),
    path('isuzucars/',views.isuzucars,name='isuzucars'),
    path('volvocars/',views.volvocars,name='volvocars'),
    path('volkswagencars/',views.volkswagencars,name='volkswagencars'),
    path('hyundaicars/',views.hyundaicars,name='hyundaicars'),
    path('mazdacars/',views.mazdacars,name='mazdacars'),
    path('lexuscars/',views.lexuscars,name='lexuscars'),
    path('kiacars/',views.kiacars,name='kiacars'),
    path('subarucars/',views.subarucars,name='subarucars'),
    path('mercedesbenzcars/',views.mercedesbenzcars,name='mercedesbenzcars'),   
    path('mitsubishicars/',views.mitsubishicars,name='mitsubishicars'),
    
    path('landrovercars/',views.landrovercars,name='landrovercars'),
    # path('search_results/', SearchResultsView.as_view(),name='search_results'),
    path('search_results/',views.searchresults,name='search_results'),
]