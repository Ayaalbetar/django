from django.shortcuts import render,redirect
from  django.contrib import messages
from services.models import person,orders,contact,services,ffamily,Advertising
import  re
########################################################
import  os
from django.http import HttpResponse
import mimetypes
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from barcode import EAN13,EAN8
from barcode.writer import ImageWriter
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import cv2
from  ALber2 import settings


#################################################
def allhos(request,):
    return render(request,'services/hospitail/allhos.html')
#################################################
def albir_eye(request,):
    return render(request,'services/hospitail/albir_eye.html')

#####################-----------------------###############
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
import imageio.v2 as iio
def student (request,):
    if request.method == 'POST' and 'btnsign' in request.POST:
        # variabls for  fields
        name=None
        email=None
        fname=None
        iid=None#الرقم الوطني
        mname=None
        berithday=None
        phone1=None
        phone2=None
        gender=None
        address=None
        photos=None
        if 'phone1' in request.POST:
            phone1 = request.POST['phone1']
        else:
            messages.error(request, 'error in phone1')
        if 'phone2' in request.POST:
            phone2 = request.POST['phone2']
        else:
            messages.error(request, 'error in phone2')
        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'error in phone2')


        if 'name' in request.POST:
            name = request.POST['name']
        else:
            messages.error(request, 'error in name')
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'error in email')
        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'error in fname')
        if 'iid' in request.POST:
            iid ="166666666"# request.POST['iid']
            #if str(iid).__len__() != 11:
             #   messages.success(request, " الرقم الوطني غير صالح")
              #  return render(request, 'services/soial/student.html')
        else:
            messages.error(request, 'error in iid')
        if 'mname' in request.POST:
            mname= request.POST['mname']
        else:
            messages.error(request, 'error in mname')
        if 'berithday' in request.POST:
            berithday= request.POST['berithday']
        else:
            messages.error(request, 'error in  berithday')
        if 'phone1' in request.POST:
            phone1 = request.POST['phone1']
        else:
            messages.error(request, 'error in phone1')
        if 'phone2' in request.POST:
            phone2 = request.POST['phone2']
        else:
            messages.error(request, 'error in phone2')
        if 'gender' in request.POST:
            gender = request.POST['gender']
            if gender =='ذكر':
                gender='ذكر'
            else :gender='أنثى'
        else:
            messages.error(request, 'error in الجنس')
        if name and fname and mname and berithday and gender and iid and email:
            if person.objects.filter(id_number=iid).exists() and \
                    orders.objects.filter(idserv=1).exists():
                messages.error(request, 'لقد سجلت مسبقا في هذه الخدمة!!! ')
            else:
                num = str(iid)
                code = EAN8(num, writer=ImageWriter())
                namebar = name +fname + str(iid)
                sdddd=code.save('media/images/' + namebar, )
                print(sdddd)
                def user_directory_path(instance, filename):
                    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                    return 'user_{0}/{1}'.format(instance.id_number, filename)

                # add student profile
                def user_directory_path(instance, filename):
                    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                    return 'user_{0}/{1}'.format(instance.id_number, filename)

                student = person(pername=name, fathername=fname, mothername=mname,
                                 id_number=iid, birthday=berithday, email=email, familyumber=0,
                                 gender=gender, barcode=int(str(code)))

                photos = request.FILES.get("f1")
                student.photo = photos
                student.save()
                # student.photo =x
                # print(x)
                student.save()
                photos = request.FILES.get("f2")
                student.photo = photos
                student.save()
                photos = request.FILES.get("f3")
                student.photo = photos
                student.save()
                photos = request.FILES.get("f4")
                student.photo = photos
                student.save()
                photos = request.FILES.get("f5")
                student.photo = photos
                student.save()
                photos = request.FILES.get("f6")
                student.photo = photos
                student.save()
                photos = request.FILES.get("f7")
                student.photo = photos
                student.save()
                photos = request.FILES.get("f8")
                student.photo = photos
                student.save()

                id = person.objects.get(pername=name, fathername=fname, mothername=mname,
                                        id_number=iid, birthday=berithday, email=email, familyumber=0,
                                        gender=gender, barcode=int(str(code)))
                contact1 = contact(tele=phone1, phone=phone2, job='', placejob='', personcontact=id)
                contact1.save()
                id2 = services.objects.get(sername='كفالة طالب')
                orders1 = orders(idperson=id, idserv=id2)
                orders1.save()
                messages.error(request, 'أهلا بك تم تسجيل طلبك  ')
                messages1 = 'jjj'
                img = id.imgbarcode
               # img=Advertising.objects.get(pk=1)
               # img=img.photo
                subject = 'llll'
                html_content = render_to_string('email_template.html',
                                                {'content': messages1, 'title': subject,'img':img })
                text_content = strip_tags(html_content)
                email11 = EmailMultiAlternatives(
                 "tesssting",
                 text_content,
                 settings.EMAIL_HOST_USER,
                 [email]
                 )
                img=id.imgbarcode
                print('////////////')
                print(img)
                print('////////////////////////')
                email11.attach(img.name, img.read())
                email11.attach_alternative(html_content, "text/html")
                email11.send()
                name1=name
                email1=email
                messages1='jjj'
                subject='llll'

                #pla pla
               # img = w.photo
                #eeeee='''<img src='media/images/tvpg999999.png'>'''
                #html_content=render_to_string('email_template.html',{'content':messages1, 'title':subject,'img':img})
                #text_content=strip_tags(html_content)
                #email11=EmailMultiAlternatives(
                 #   "tesssting",
                  #  text_content,
                   # settings.EMAIL_HOST_USER,
                    #[email]
                #)
                #email11.attach_alternative(html_content,"text/html")
                #email11.send()
                #template=loader.get_template('contact_form.txt')
                #cont={
                 #   'name1':name, 'email1':email,'message1':messages1,'subject':subject
                  #,'namebar':namebar }
                #messages1=template.render(cont)
                #email2=EmailMultiAlternatives(
                 #   "you got a proo",messages1,
                  #  "company x"+"- Good",
                   #     [email]
                #)
                #img = cv2.imread('media/images/' + namebar, 0)
                #iop=open(sdddd)
                #email2.content_subtype='html'
                #file=iop

                #email2.attach(file.name,file.read())
                #email2.send()





        else:
            messages.error(request, 'هناك حقول فارغة ')
        context= {
           'name' :name,
            'email': email,
            'fname' : fname,
            'iid' : iid,
            'mname' : mname,
            'berithday' :berithday

        }


    else:
      context={}
    return render(request,'services/soial/student.html',context)

#########################--------------------##############
def orphan (request,):
    if request.method =='POST': #and 'btnsign' in request.POST:
        name = None
        email = None
        fname = None
        iid = None  # الرقم الوطني
        mname = None
        phone1 = None
        phone2 = None
        gender = None
        address = None
        photos = None
        num_fmal=None
        num_mal=None
        num_family=None
        income_type=None
        if 'phone1' in request.POST:
            phone1 = request.POST['phone1']
        else:
            messages.error(request, 'error in phone1')
        if 'phone2' in request.POST:
            phone2 = request.POST['phone2']
        else:
            messages.error(request, 'error in phone2')
        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'error in address')
        if 'name' in request.POST:
            name = request.POST['name']
        else:
            messages.error(request, 'error in name')

        if 'fname' in request.POST:
            fname = request.POST['fname']
        if 'email' in request.POST:
            email=request.POST['email']
        if  'iid' in request.POST:
            iid=request.POST['iid']
        else: messages.error(request,'kkkkkkkkkkk')
        if 'num_fmal' in request.POST:
            num_fmal=request.POST['num_fmal']
        else:
            messages.error(request, 'error in num_fmal')
        if 'num_mal' in request.POST:
            num_mal=request.POST['num_mal']
        else:
            messages.error(request, 'error in num_mal')
        if 'num_family' in request.POST:
            num_family=request.POST['num_family']
        else:
            messages.error(request, 'error in num_family')
        if 'income_type' in request.POST:
            income_type= request.POST['income_type']
        else:
            messages.error(request, 'error in imcome_type')
        if iid  :
            if person.objects.filter(id_number=iid).exists() and \
                    orders.objects.filter(idserv=2).exists():
                messages.error(request, 'لقد سجلت مسبقا في هذه الخدمة!!! ')
            else:
                num = str(iid)
                code = EAN8(num, writer=ImageWriter())
                namebar = name + fname + str(iid)
                code.save('media/images/' + namebar, )

                # add student profile
                def user_directory_path(instance, filename):
                    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                    return 'user_{0}/{1}'.format(instance.id_number, filename)
                orphan= person(pername=name,fathername=fname,
                             id_number=iid, birthday=None,
                             email=email, familyumber=num_family,
                            incometype=income_type,
                             barcode=int(str(code)))
                photos = request.FILES.get("f1")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f2")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f3")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f4")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f5")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f6")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f7")
                orphan.photo = photos
                orphan.save()
                photos = request.FILES.get("f8")
                orphan.photo = photos
                orphan.save()
                id=person.objects.get(pername=name, fathername=fname,
                                        id_number=iid,
                                         barcode=int(str(code)))
                family1 = ffamily(num_male=num_mal, num_fmale=num_fmal, family_id=id)
                family1.save()

                contact1 = contact(tele=phone1, phone=phone2, job='', placejob='', personcontact=id)
                contact1.save()

                id2 = services.objects.get(sername='كفالة يتيم')
                orders1 = orders(idperson=id, idserv=id2)
                orders1.save()
                messages.error(request, 'أهلا بك تم تسجيل طلبك  ')
        else:
            messages.error(request, 'lllllllllllllllllll  ')

    return render(request,'services/soial/orphan.html')


################################
def basket(request):
    if request.method == 'POST' and 'btnsign' in request.POST:
        name=None
        fname=None
        mname=None
        email=None
        num_family=None
        iid=None
        phone1=None
        phone2=None
        job=None
        place_jop=None
        address=None
        income_type=None
        average_income=None
        dis_situ=None
        place_disp=None
        hom_situ=None
        num_mal=None
        num_fmal=None
        o_num=None
        w_num=None
        if 'phone1' in request.POST:
            phone1 = request.POST['phone1']
        else:
            messages.error(request, 'error in phone1')
        if 'name' in request.POST:
            name = request.POST['name']
        else:
            messages.error(request, 'error in name')
        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'error in fname')
        if 'mname' in request.POST:
            mname = request.POST['mname']
        else:
            messages.error(request, 'error in mname')
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'error in email')
        if 'num_family' in request.POST:
            num_family = request.POST['num_family']
        else:
            messages.error(request, 'error in num_family')
        if 'iid' in request.POST:
            iid = "12345678"#request.POST['iid']
        else:
            messages.error(request, 'error in iid')
        if 'job' in request.POST:
            job = request.POST['job']
        else:
            messages.error(request, 'error in job')
        if 'place_jop' in request.POST:
            place_jop=request.POST['place_jop']
        else:
            messages.error(request, 'error in place_jop')
        if 'address' in request.POST:
            address=request.POST['address']
        else:
            messages.error(request,'error in address')
        if 'income_type' in request.POST:
            income_type=request.POST['income_type']
        else:messages.error(request,'error in income_type')
        if 'average_income' in request.POST:
            average_income=request.POST['average_income']
        else:
            messages.error(request,'error in address')
        if 'dis_situ' in request.POST:
            dis_situ=request.POST['dis_situ']
        else:
            messages.error(request,'error in dis_situ')
        if 'place_disp' in request.POST['place_disp']:
            place_disp=request.POST['place_disp']
        else:messages.error(request,'error in place_disp')

        if 'hom_situ' in request.POST['hom_situ']:
            hom_situ= request.POST['hom_situ']
        else:
            messages.error(request,'error in hom_situ')
        if 'num_mal'in request.POST:
            num_mal=request.POST['num_mal']
        else:messages.error(request,'error in num_mal')
        if 'num_fmal'in request.POST:
            num_fmal=request.POST['num_fmal']
        else:messages.error(request,"error in num_fmal")
        if 'o_num'in request.POST:
            o_num=request.POST['o_num']
        else:messages.error(request,"error in num_fmal")
        if 'w_num'in request.POST:
            w_num=request.POST['w_num']
        else:messages.error(request, "error in w_num")
        if iid  :
            if person.objects.filter(id_number=iid).exists() and \
                    orders.objects.filter(idserv=7).exists():
                messages.error(request, 'لقد سجلت مسبقا في هذه الخدمة!!! ')
            else:
                num = str(iid)
                code = EAN8(num, writer=ImageWriter())
                namebar = name + fname + str(iid)
                code.save('media/images/' + namebar, )

                def user_directory_path(instance, filename):
                    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                    return 'user_{0}/{1}'.format(instance.id_number, filename)
                ser=services.objects.get(types=1)
                numser=ser. number_person
                numper=numser+1
                basket = person(pername=name, fathername=fname, mothername=mname, incometype=income_type,
                                id_number=iid, birthday=None, sheltercondition=hom_situ, avaregeincom=average_income,
                                email=email, familyumber=num_family,
                                address=address,
                                barcode=int(str(code)))
                photos = request.FILES.get("f1")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f2")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f3")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f4")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f5")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f6")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f7")
                basket.photo = photos
                basket.save()
                photos = request.FILES.get("f8")
                basket.photo = photos
                basket.save()
                id = person.objects.get(barcode=int(str(code)), id_number=iid)
                contact1 = contact(tele=phone1, phone=phone1, job=job, placejob=place_jop, personcontact=id)
                contact1.save()


                family1 =ffamily(family_id=id,num_male=num_mal,num_fmale=num_fmal,
                           trestles=w_num,elderliness=o_num, )
                family1.save()
                id2 = services.objects.get(sername='سلة غذائية')
                orders1 = orders(idperson=id, idserv=id2 ,number_person=numper)
                sernew=services.objects.get(pk=id2.pk)
                sernew.number_person=numper
                sernew.save()
                orders1.save()
                messages.error(request, 'أهلا بك تم تسجيل طلبك  ')


        else:
            messages.error(request, 'lllllllllllllllllll  ')



    return render(request,'services/basket/basket.html')



def medican(request):
    return render(request,'services/soial/medican.html')
def patient(requrst):
    return render(requrst,'services/soial/patient.html')
def family(request):
    return render(request,'services/soial/family.html')