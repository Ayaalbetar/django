from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
#import stripe
from .models import services,Advertising
# Create your views here.
from barcode import EAN13
from barcode.writer import ImageWriter
from  services import  models,views
from django.shortcuts import render
import  folium
from folium import plugins, features
import geocoder
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

from map.models import Map_location
def index(request):
    if request.method == 'POST' and 'btnsign' in request.POST:
        subject = request.POST["subject"]

        email = request.POST.get("email")

        message = request.POST.get("message")
        send_mail(
            subject,
            message,
            email,
            ['albirr2000albir@gmail.com'],
            # settings.ADMIN_EMAILS
                       )


    new = Map_location.objects.all()
    location = geocoder.osm('homs')
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[34.73121, 36.70564], zoom_start=10)
# folium.Marker([20.594,-0.219]).add_to(m)
# folium.Marker([lat,lng],tooltip='انقر هنا',popup=country).add_to(m)
    c=0
    cc=[]
    for i in new:
        c=c+1

        if i.user_count!=0:
         print('kkkkkk')
         folium.Marker([i.lat, i.lng], tooltip='انقر هنا', popup=i.activity_name+" "+str(i.user_count),
                         #icon=folium.Icon(icon='glyphicon-plane', prefix='glyphicon')
                         ).add_to(m)
        else:

            print("jjjjjjj")
            folium.Marker([i.lat, i.lng], tooltip='انقر هنا',
          # icon=folium.Icon(icon_color='red',icon='cloud',
                     icon=plugins.BeautifyIcon(number=c,border_color='blue',border_width=1,text_color='red',inner_icon_style='margin-top:0px;')
                         #icon=folium.Icon(color='green',icon='bolt', )
                        , popup=i.locations_name,).add_to(m)
    title = 'جمعية البر والخدمات الاجتماعية '
    m = m._repr_html_()

# من اجل الباركود
  #  num = '1111111111111'
    #code = EAN13(num, writer=ImageWriter())
   # code.save("new code1111")
  #  return render(request,'part/base.html')
  #####


    context={

        'ad': Advertising.objects.all(),
        'm': m,
        "template":title, }


    return render(request,'services/index.html',context)
    #return render(request,'index3.html')
    #return render(request,'admin1.html')



# Create your views here.






def services(request,):
    context={}
    return render(request,'services/services.html',context)

def about(request):
    return render(request,'services/about.html')
def projects(request):
    return render(request,'services/projects.html')

def success(request):
    return render(request,'part/success.html')


from django.core.mail import send_mail
from  django.contrib import messages
from  .models import  person,orders
from  django.conf import settings

def contact (request,):
    x=None
    if request.method == 'POST' and 'btnsign' in request.POST:
        p=person.objects.filter(isseen=True ,sendemail=True)
        if p.exists():# and ord.exists():
            for e in p :
                 ord = orders.objects.filter(idperson=e.pk, status_order='تم قبوله')
                 if ord.exists():
                     subject = request.POST["subject"]
                     # email=request.POST["email"]
                     email = e.email
                     message = request.POST["message"]
                     send_mail(
                         subject,
                         message,
                         settings.EMAIL_HOST_USER,
                         [email],

                         #  fail_silently=False,
                     )
                     e.sendemail=False
                     e.save()
                     x=e
                     messages.success(request, 'تم ارسال الرسالة')
            x=p
            #return render(request, 'part/success.html',{'x':x})
        x=p
    return render(request,'contact/contact.html',{'x':x})
# notifications
def notifs(request):
    data=models.Notify.objects.all().order_by('-id')
    return  render(request,'services/notifs.html',{'data':data})

from .models import NotifUserStatus
from django.core import serializers
from django.http import JsonResponse
#get all notifications
def get_notifs(request):
    data=models.Notify.objects.all().order_by('-id')
    notifStatus=False
    jsonData=[]
    for d in data:

            notifStatusData=NotifUserStatus.objects.get(user=request.user,notif=d,)
            if notifStatusData :
                notifStatus=True
            jsonData.append({
                'pk': d.id,
                'notify_detail': d.notify_detail,
                'notifStatus': notifStatus
            })

         #jsonData=serializers.serialize('json',data)
    return JsonResponse({'data':jsonData})

def getnotif(request):
    data=models.notif_addnew.objects.all().order_by('-id')
    ord = models.orders.objects.filter(pk=data[0].id)
    print(ord)
    #ord=None
    #j=None
    #for d in data:
      # ord=models.orders.objects.filter(pk=d.pk)
       #print(ord)

     #  j=serializers.serialize('json', ord)
     #  print(j)
    #j = serializers.serialize('json', ord)
    jsonData=serializers.serialize('json',data)
    return  JsonResponse({'ord':jsonData})

def nn(request):
    data = models.notif_addnew.objects.all().order_by('-id')
    return render(request, 'services/no.html', {'data': data})


# mark read by user
def mark_read_notif(request):
    notif=request.GET['notif']
    notif=models.Notify.objects.get(pk=notif)
    user=request.user
   # v=models.NotifUserStatus.objects.filter(notif=notif,user=user,)
   # if v.exists():
    #    pass
    #else:
    models.NotifUserStatus.objects.create(notif=notif,user=user, status=True)
    return JsonResponse({'bool':True})
