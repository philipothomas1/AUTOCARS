from django.shortcuts import render,get_object_or_404
from .models import Cars,Make,Trannsmission,Drive,FuelType,BodyType,Cars,AutoParts,ContactInfomation,HomeBanner1,HomeBanner2,SideBanner1,SideBanner2,SideBanner3
from django.views.generic import ListView, DetailView,View
from .forms import SearchForm
from django.db.models import Sum,Count
# Create your views here.
from django.db.models import Q

# class SearchResultsView(ListView):
#     model = Cars
#     template_name = 'search_results.html'
#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         # info=ContactInfomation.objects.filter()
#         # if query:

#         object_list = Cars.objects.filter(
#             Q(car_name__icontains=query) | Q(price__icontains=query) | Q(mileage__icontains=query)
#         )
#         return object_list

def searchresults(request):
	query =request.GET.get('q')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	object_list = Cars.objects.filter( Q(car_name__icontains=query) | Q(price__icontains=query) | Q(mileage__icontains=query))
	context={"object_list":object_list,"info":info,"newarrivals":newarrivals,"autoparts":autoparts}
	return render(request,"search_results.html",context)




def home(request):

	queryset=Cars.objects.filter().order_by('-added_on')
	homebanner1=HomeBanner1.objects.filter()
	homebanner2=HomeBanner2.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	form=SearchForm(request.POST or None)
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	toyota = Make.objects.filter(make_name__contains='toyota').annotate(toyota_count=Count('cars'))
	nissan = Make.objects.filter(make_name__contains='nissan').annotate(nissan_count=Count('cars'))
	bmw = Make.objects.filter(make_name__contains='bmw').annotate(bmw_count=Count('cars'))
	audi = Make.objects.filter(make_name__contains='audi').annotate(audi_count=Count('cars'))
	count_toyota=[make.toyota_count*1 for make in toyota]
	num_of_toyota=count_toyota[0]
	toyota1 = Make.objects.filter(make_name__contains='toyota').annotate(toyota_count=Count('cars'))

	count_nissan=[make.nissan_count*1 for make in nissan]
	num_of_nissan=count_nissan[0]

	count_bmw=[make.bmw_count*1 for make in bmw]
	num_of_bmw=count_bmw[0]

	count_audi=[make.audi_count*1 for make in audi]
	num_of_audi=count_audi[0]

	qs = Cars.objects.filter(price__gte= 30000000)
	info=ContactInfomation.objects.filter()
	#toyota5 = Make.objects.filter(make_name__contains='toyota').
	#qse=Make.objects.filter(cars__in=Cars.objects.filter(make_name='TOYOTA'))
	#print(qs)
	#nissan = Make.objects.filter(make_name__contains='nissan').annotate(nissan_count=Count('cars'))
	#qes = Cars.objects.select_related('make__make_name').get(id=2)
	m1=Make.objects.get(id=1)
	c1=m1.cars_set.all()

	m2=Make.objects.get(id=2)
	c2=m2.cars_set.all()

	m3=Make.objects.get(id=3)
	c3=m3.cars_set.all()

	m4=Make.objects.get(id=4)
	c4=m4.cars_set.all()

	m5=Make.objects.get(id=5)
	c5=m5.cars_set.all()

	m6=Make.objects.get(id=6)
	c6=m6.cars_set.all()

	# m7=Make.objects.get(id=1)
	# c7=m7.cars_set.all()

	# m8=Make.objects.get(id=1)
	# c8=m8.cars_set.all()
	# qes=Cars.objects.filter().select_related(make__eq='toyota')
	


	#nissan = Make.objects.filter(name__contains='nissan').annotate(nissan_count=Count('Cars'))
	
	context={
	"queryset":queryset,
	'autoparts':autoparts,
	'toyota':toyota,
	'nissan':nissan,
	'bmw':bmw,
	'audi':audi,
	'num_of_toyota':num_of_toyota,
	'num_of_nissan':num_of_nissan,
	'num_of_bmw':num_of_bmw,
	'num_of_audi':num_of_audi,
	'qs':qs,

	'c1':c1,
	'c2':c2,
	'c3':c3,
	'c4':c4,
	'c5':c5,
	'c6':c6,
	"newarrivals":newarrivals,
	"info":info,
	"homebanner1":homebanner1,
	"homebanner2":homebanner2


	}

	return render(request, "index.html",context)


def car_detail(request,slug):
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	m1=Make.objects.get(id=1)
	c1=m1.cars_set.all()
	m4=Make.objects.get(id=1)
	c4=m4.cars_set.all()
	detail = get_object_or_404(Cars, slug = slug)

	toyota = Make.objects.filter(make_name__contains='toyota').annotate(toyota_count=Count('cars'))
	nissan = Make.objects.filter(make_name__contains='nissan').annotate(nissan_count=Count('cars'))
	bmw = Make.objects.filter(make_name__contains='bmw').annotate(bmw_count=Count('cars'))
	audi = Make.objects.filter(make_name__contains='audi').annotate(audi_count=Count('cars'))
	count_toyota=[make.toyota_count*1 for make in toyota]
	num_of_toyota=count_toyota[0]
	toyota1 = Make.objects.filter(make_name__contains='toyota').annotate(toyota_count=Count('cars'))

	count_nissan=[make.nissan_count*1 for make in nissan]
	num_of_nissan=count_nissan[0]

	count_bmw=[make.bmw_count*1 for make in bmw]
	num_of_bmw=count_bmw[0]

	count_audi=[make.audi_count*1 for make in audi]
	num_of_audi=count_audi[0]

	print(info)
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={
	"detail":detail,
	"c1":c1,
	"c4":c4,
	'toyota':toyota,
	'nissan':nissan,
	'bmw':bmw,
	'audi':audi,
	'num_of_toyota':num_of_toyota,
	'num_of_nissan':num_of_nissan,
	'num_of_bmw':num_of_bmw,
	'num_of_audi':num_of_audi,
	"newarrivals":newarrivals,
	"info":info,
	'autoparts':autoparts,
	}
	return render (request,'car_detail.html',context)


# class spare_detail(DetailView):
# 	model=AutoParts

# 	template_name="spare_detail.html"
# 	context_object_name = 'object_list'
# 	filter = AutoParts.objects.filter().order_by('-spare_parts_name')


# 	def get_queryset(self):
# 		return AutoParts.objects.all()
        

# 	def get_context_data(self, **kwargs):
# 	    ctx = super(spare_detail, self).get_context_data(**kwargs)
# 	    ctx['filter'] = AutoParts.objects.filter().order_by('-spare_parts_name')
# 	    return ctx


def spare_detail(request,slug):
	info=ContactInfomation.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	detail = get_object_or_404(AutoParts, slug = slug)
	toyota = Make.objects.filter(make_name__contains='toyota').annotate(toyota_count=Count('cars'))
	nissan = Make.objects.filter(make_name__contains='nissan').annotate(nissan_count=Count('cars'))
	bmw = Make.objects.filter(make_name__contains='bmw').annotate(bmw_count=Count('cars'))
	audi = Make.objects.filter(make_name__contains='audi').annotate(audi_count=Count('cars'))
	count_toyota=[make.toyota_count*1 for make in toyota]
	num_of_toyota=count_toyota[0]
	toyota1 = Make.objects.filter(make_name__contains='toyota').annotate(toyota_count=Count('cars'))

	count_nissan=[make.nissan_count*1 for make in nissan]
	num_of_nissan=count_nissan[0]

	count_bmw=[make.bmw_count*1 for make in bmw]
	num_of_bmw=count_bmw[0]

	count_audi=[make.audi_count*1 for make in audi]
	num_of_audi=count_audi[0]

	context={
	"detail":detail,
	'num_of_toyota':num_of_toyota,
	'num_of_nissan':num_of_nissan,
	'num_of_bmw':num_of_bmw,
	'num_of_audi':num_of_audi,
	"newarrivals":newarrivals,
	"info":info,
	'autoparts':autoparts,
	}
	return render (request,'spare_detail.html',context)



def toyotacars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m1=Make.objects.get(id=1)
	c1=m1.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c1":c1,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'toyota.html',context)

def nissancars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m2=Make.objects.get(id=2)
	c2=m2.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c2":c2,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'nissan.html',context)

def fordcars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m3=Make.objects.get(id=3)
	c3=m3.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c3":c3,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'ford.html',context)

def bmwcars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m4=Make.objects.get(id=4)
	c4=m4.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c4":c4,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'bmw.html',context)
    
def audicars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m5=Make.objects.get(id=5)
	c5=m5.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c5":c5,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'audi.html',context)

def jeepcars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m6=Make.objects.get(id=6)
	c6=m6.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c6":c6,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'jeep.html',context)

def hondacars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m7=Make.objects.get(id=7)
	c7=m7.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c7":c7,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'honda.html',context)

def suzukicars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m8=Make.objects.get(id=8)
	c8=m8.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c8":c8,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'suzuki.html',context)
    
def isuzucars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m9=Make.objects.get(id=9)
	c9=m9.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c9":c9,"newarrivals":newarrivals,'autoparts':autoparts,"info":info,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'isuzu.html',context)

def volvocars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m10=Make.objects.get(id=10)
	c10=m10.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c10":c10,"newarrivals":newarrivals,"info":info,"autoparts":autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'volvo.html',context)

def volkswagencars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m11=Make.objects.get(id=11)
	c11=m11.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c11":c11,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'volkswagen.html',context)

def hyundaicars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m12=Make.objects.get(id=12)
	c12=m12.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c12":c12,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}

	return render (request,'hyundai.html',context)
def mazdacars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m13=Make.objects.get(id=13)
	c13=m13.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c13":c13,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'mazda.html',context)

def lexuscars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m14=Make.objects.get(id=14)
	c14=m14.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c14":c14,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'lexus.html',context)

def kiacars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m15=Make.objects.get(id=15)
	c15=m15.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c15":c15,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'kia.html',context)

def subarucars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m16=Make.objects.get(id=16)
	c16=m16.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c16":c16,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'subaru.html',context)

def mercedesbenzcars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m17=Make.objects.get(id=17)
	c17=m17.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c17":c17,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'mercedesbenz.html',context)

def mitsubishicars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m18=Make.objects.get(id=18)
	c18=m18.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c18":c18,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'mitsubishi.html',context)

def landrovercars(request):
	sidebanner1=SideBanner1.objects.filter()
	sidebanner2=SideBanner2.objects.filter()
	sidebanner3=SideBanner3.objects.filter()
	autoparts=AutoParts.objects.filter().order_by('-added_on')
	info=ContactInfomation.objects.filter()
	newarrivals=Cars.objects.filter().order_by('-added_on')[0:4]
	m19=Make.objects.get(id=19)
	c19=m19.cars_set.all()
	# print(qes)
	#qs = Cars.objects.select_related('cars__make')
	context={"c19":c19,"newarrivals":newarrivals,"info":info,'autoparts':autoparts,"sidebanner1":sidebanner1,"sidebanner2":sidebanner2,"sidebanner3":sidebanner3}
	return render (request,'landrover.html',context)


    
    