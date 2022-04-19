from django.db import models
from django.db.models.signals import post_save,pre_delete,pre_save
from django.utils.html import mark_safe
from  django.dispatch import receiver

# Create your models here.

#class category(models.Model):
 #   name=models.CharField(max_length=500)

  #  def __str__(self):
   #     return self.name



from datetime import date
class person (models.Model):
    blod=[
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),  ]
    gender=[('fmale','أنثى'),
            ('male','ذكر'),]
    pername=models.CharField(max_length=20,default=None,verbose_name='الاسم الكامل')
    fathername=models.CharField(max_length=20,default=None)
    mothername=models.CharField(max_length=100,blank=True)
    id_number=models.IntegerField(default=0)
    familyumber=models.PositiveIntegerField(default=None,blank=True)
    birthday = models.DateField(default=date.today, blank=True,null=True)
    gender=models.CharField(max_length=5,default=None ,null=True,blank=True)#,choices=gender)
    email= models.EmailField(default=None)
    education=models.CharField(max_length=90,default=None,blank=True,null=True)
    barcode=models.IntegerField(default=0,blank=True,null=True)
    blod=models.CharField( max_length=90,default=None,choices=blod,null=True,blank=True)
    helth=models.CharField(max_length=90,default=None,null=True,blank=True)
    avaregeincom=models.DecimalField(max_digits=6,decimal_places=2,null=True,default=None,blank=True)#متوسط الدخل
    socialstatus=models.CharField(max_length=200,default=None,null=True,blank=True)#الحالة الاجتماعية
    sheltercondition =models.CharField(max_length=100,default=None ,null=True,blank=True)#حالة المأوى
    incometype=models.CharField(max_length=100 ,default=None ,null=True,blank=True)#نوع الدخل
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100,default=None, null=True,blank=True)
    amount_money = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    isseen = models.BooleanField(default=False,verbose_name='تمت مشاهدته')
    sendemail = models.BooleanField(default=False,verbose_name='ارسال رسالة ')
    imgbarcode=models.ImageField(upload_to='images/',null=True,blank=True)
    def user_directory_path(instance, filename):
            # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
            return 'user_{0}/{1}'.format(instance.id_number, filename)

    photo = models.FileField(upload_to=user_directory_path, null='True')

    class Meta:
        verbose_name = "المستفيد"
        verbose_name_plural = "المستفيدين"



    def __str__(self):
            return f"{self.pername }   {self.fathername}"

#هون من أجل توليد باركود للشخص قبل الحفظ من الادمن
from barcode import EAN13,EAN8
from barcode.writer import ImageWriter
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import cv2
from  ALber2 import settings
def generate_barcode(sender,**Kwargs):
    if Kwargs['created']:
       pe = Kwargs['instance']
       num=pe.id_number
       num=str(num)
       code = EAN8(num, writer=ImageWriter())
       pe.barcode = int(str(code))
       pe.save()
       namebar =pe.pername +pe.fathername + str(pe.id_number)
       c=code.save('media/images/'+ namebar, )
       c=c[6:]
       pe.imgbarcode=c
       pe.save()
      # code.save('media/images/' + namebar, )

#def pre_saveper(sender,**Kwargs):
       # pla
      # pe = Kwargs['instance']
       #messages1 = 'jjj'
       #subject = 'llll'

       #img = pe.imgbarcode
       #img='Users\PcMax\Desktop\project\media'+img
       #print(img)
       #html_content = render_to_string('email_template.html', {'content': messages1, 'title': subject, 'img': img})
       #text_content = strip_tags(html_content)
       #email11 = EmailMultiAlternatives(
        #   "tesssting",
         #  text_content,
          # settings.EMAIL_HOST_USER,
          # ['ayoshbetar2000@gmail.com']
       #)
       #email11.attach(img.name, img.read())
    #   email11.attach_alternative(html_content, "text/html")
       #email11.send()
post_save.connect(generate_barcode,sender=person)
#post_save.connect(pre_saveper,sender=person)



class ffamily(models.Model):
       #c=models.CharField(default=None,max_length=1)
       num_male=models.PositiveIntegerField(default=None,null=True,blank=True, verbose_name='عدد الذكور')
       num_fmale=models.PositiveIntegerField(default=None,null=True,blank=True, verbose_name='عدد الإناث')
       trestles=models.PositiveIntegerField(default=None,null=True,blank=True, verbose_name='عدد الحوامل')
       elderliness=models.PositiveIntegerField(default=None,null=True,blank=True, verbose_name='عدد الكهول')
       family_id = models.OneToOneField(person, on_delete=models.CASCADE, primary_key=True, verbose_name='اسم الشخص')
       class Meta:
           verbose_name="عائلةالمستفيد"
           verbose_name_plural ="عائلات المستفيدين"
       def __str__(self):
           x=self.family_id
           x1=str(x)
           return  x1

class contact(models.Model):
    tele=models.IntegerField(default=0, verbose_name='رقم الهاتف')
    phone=models.IntegerField(default=0, verbose_name='رقم الجوال')
    job=models.CharField(max_length=100, verbose_name='العمل')
    placejob=models.CharField(max_length=100, verbose_name='مكان العمل')
    job2=models.CharField(max_length=100, blank=True, verbose_name='عمل أخر')
    personcontact=models.OneToOneField(
         person,
         on_delete=models.CASCADE,
         primary_key=True, verbose_name='اسم المستفيد'
            )

    class Meta:
        verbose_name = "تواصل مع المستفيد"
        verbose_name_plural="تواصل"

    def __str__(self):return str(self.personcontact)




class services(models.Model):
    x = [
        ('Relief', 'الاغاثة'),  # الاغاثة
        ('Social support', 'الدعم الاجتماعي'),
        ('Health care', 'المشفى')
    ]

    sername = models.CharField(max_length=100,verbose_name='اسم الخدمة')
    status = models.BooleanField(verbose_name='حالة الخدمة')  # حالة الخدمة
    number_person = models.IntegerField(default=None, blank=True, null=True,verbose_name='الدور')
    types = models.CharField(max_length=2,verbose_name='نمط')
    # idservice = models.ForeignKey(category, related_name='contain', on_delete=models.CASCADE)
    category = models.CharField(max_length=30, blank=True, default=None, choices=x,verbose_name='تصينف الخدمة')
    positions = models.CharField(max_length=100, blank=True, default=None,verbose_name='مكان الخدمة')
    contact = models.ManyToManyField(person, through='orders',verbose_name='')

    def __str__(self):
        return self.sername

    class Meta:
        verbose_name = "الخدمة"
        verbose_name_plural="الخدمات"
class orders(models.Model):

    idperson = models.ForeignKey(person, related_name='order', on_delete=models.CASCADE, verbose_name='اسم المستفيد')
    idserv = models.ForeignKey(services, related_name='order', on_delete=models.CASCADE, verbose_name='اسم الخدمة')
    status_order=models.CharField(max_length=20, verbose_name='حالة الطلب')#حالة الطلب مفعل -قيد الدراسة -الخ
    date_order=models.DateTimeField(auto_now_add=True , verbose_name='تاريخ الطلب')
    number_person = models.IntegerField( default=None,blank=True,null=True, verbose_name='الدور')

    class Meta:
        verbose_name = "الطلب"
        verbose_name_plural="الطلبات"

    def save(self,*args,**kwargs,):
        super(orders,self).save(*args,**kwargs)




#من أجل السلة الغذائية ومن اجل المشافي
# من أجل اذا تم اضافة طلب جديد يتم زيادة الدور في الخدمة ويتم اضافة القيمةالى حقل الدور في الطلب
def increase_number_person_services(sender,**kwargs):
    if kwargs['created']:
        increase_number = kwargs['instance']
        idserveord = increase_number.idserv
        serv = services.objects.get(pk=idserveord.id)
        if serv.types == '1':
           increase_number.number_person=serv.number_person+1
           increase_number.save()
           serv.number_person = serv.number_person + 1
           serv.save()
post_save.connect(increase_number_person_services,sender=orders)
#من أجل اذا تمحذف الطلب  يتمانقاص حقل الدور
def decrease_number_person(sender,**Kwargs):
       del_order=Kwargs['instance']
       delorder=del_order.number_person
       idservord=del_order.idserv
       serv=services.objects.get(pk=idservord.id)
       if serv.types=='1':
           del_orders = orders.objects.filter(idserv=serv.id)
           for o in del_orders:
               o.number_person = o.number_person - 1
               if o.number_person <= 0:
                   o.number_person = 0
               o.save()
           serv.number_person = serv.number_person - 1
           serv.save()

pre_delete.connect(decrease_number_person,sender=orders)






class notif_addnew(models.Model):
    ord = models.OneToOneField(person, on_delete=models.CASCADE)
    isread = models.BooleanField( default=False)
    def __str__(self):
        #return str(self.ord.idperson)
        return str(self.ord)
def create_notif(sender,**kwargs):
    if kwargs['created']:
        notif_addnew.objects.create(ord=kwargs['instance'])
        x=notif_addnew.objects.filter(isread=True).delete()

post_save.connect(create_notif,sender=person)


#class position (models.Model):#المركز
  #  name=models.CharField(max_length=40)
   # address=models.CharField(max_length=40)
    #phone=models.PositiveIntegerField()
    #contact = models.ManyToManyField(services, through='content_serv')
    #def __str__(self):
     #  return self.name

 #class content_serv(models.Model):#جدول كسر العلاقة
  #  status_serv=models.BooleanField(default=True)#حالة الخدمة
   # idposition = models.ForeignKey(position, related_name='order', on_delete=models.CASCADE)
    #idserv = models.ForeignKey(services, related_name='content', on_delete=models.CASCADE)







# اعلانات
class Advertising(models.Model):
        title = models.CharField(max_length=500)
        details = models.TextField(max_length=3000)
        date = models.DateField(auto_now_add=True)
        photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)

        def __str__(self):
            return self.title

        class Meta:
            verbose_name = "الأعلان"
            verbose_name_plural = "الإعلانات"
            ordering = ['-date']




from  django.contrib.auth.models import User


#notification
class Notify(models.Model):
    notify_detail=models.TextField()
    read_by_user =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):return str(self.notify_detail)

# markas read notification by user
class NotifUserStatus(models.Model):
    notif=models.ForeignKey(Notify,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)