from django.contrib import admin
from django.http import HttpResponse

from . import models
from  .models import Advertising,services,person,ffamily,contact,orders#content_serv,,position,
# Register your models here.
#admin.site.register(category)

#admin.site.register(content_serv)

#admin.site.register(position)
class OrdersInline(admin.TabularInline):
    model = orders
    extra = 0
class FfamilyInline(admin.TabularInline):
    model=ffamily
class ContactInline(admin.TabularInline):
    model=contact
class servicesInline(admin.TabularInline):
    model=services
    extra = 0
class personInline(admin.TabularInline):
    model=person

class AdminServices(admin.ModelAdmin):
    inlines = (OrdersInline,)
admin.site.register(services,AdminServices)
class AdminPerson(admin.ModelAdmin):
    inlines = (OrdersInline,FfamilyInline,ContactInline)
    def get_form(self, request, obj=None, **kwargs):
        form2 = super().get_form(request, obj, **kwargs)
        form2.base_fields["pername"].label = "الاسم الكامل"
        form2.base_fields["fathername"].label = "اسم الأب"
        form2.base_fields["mothername"].label = "اسم الأم"
        form2.base_fields["id_number"].label = "الرقم الوطني"
        form2.base_fields["familyumber"].label = "رقم دفتر العائلي"
        form2.base_fields["birthday"].label = "المواليد"
        form2.base_fields["gender"].label = "الجمس"
        form2.base_fields["email"].label = " البريد الالكتروني"
        form2.base_fields["education"].label = "المستوى التعليمي"
        form2.base_fields["barcode"].label = "الباركود"
        form2.base_fields["blod"].label = "زمرة الدم"
        form2.base_fields["helth"].label = "الصحة"
        form2.base_fields["avaregeincom"].label = "متوسط الدخل"
        form2.base_fields["socialstatus"].label = "الحالة الاجتماعية"
        form2.base_fields["sheltercondition"].label = "حتاة المأوى"
        form2.base_fields["incometype"].label = "نوع الدخل"
        form2.base_fields["address"].label = "العنوان"
        form2.base_fields["amount_money"].label = "المبلغ "
        form2.base_fields["photo"].label = "الصور"
        return form2;

    def ids(self, obj):
        return obj.id_number
    def persname(self, obj):
        return obj.pername
    def fa(self, obj):
        return obj.fathername
    def bar(self, obj):
        return obj.barcode
    def updates(self, obj):
        return obj.updated
    def amount(self, obj):
        return obj.amount_money


    ids.short_description='الرقم الوطني'
    persname.short_description='الاسم الكامل'
    fa.short_description = 'اسم الأب'
    bar.short_description ='الباركود'
    updates.short_description='أخر تعديل'
    amount.short_description='المبلغ'



    class Meta:
        ordering = ("updated")
    list_display = ['pername','fa','isseen','sendemail','amount','ids','email','bar','updates']
    list_filter=['pername','isseen']
    list_editable = ['isseen','sendemail']
admin.site.register(person,AdminPerson)



class AdminFfamily(admin.ModelAdmin):
    def idper(self,obj):
        return obj.family_id
    idper.short_description='اسم المستفيد'
    def numf(self,obj):
        return obj.num_fmale
    numf.short_description='عدد الإناث'
    def numm(self,obj):
        return obj.num_male
    numm.short_description='عدد الذكور'
    list_display = ['idper','numf','numm']


admin.site.register(ffamily,AdminFfamily)
admin.site.register(contact)




class AdminOrders(admin.ModelAdmin):
    def posi(self,obj):
        #x = services.objects.all()
        #x2 = orders.objects.all()
        #xxx=None
        #c=[]
        #for x1 in x:
        #  xxx=orders.objects.filter(idserv=x1.pk)
         # c.append(xxx.status_order)
        #for x1 in x:
         #   for x3 in x2:
          #     if x1.sername == x3.idserv:
           #     print('tt')
        dd=[]
        q=services.objects.filter(sername=obj.idserv)
     #   d=services.objects.filter(positions=q.positions)
        for f in q:
            d = services.objects.filter(positions=f.positions)
            for g in d:

                #print(g.positions)
                dd.append(g.positions)

        return (q[0]).positions
    def ido(self, obj):     return obj.idperson
    def ids(self, obj):    return obj.idserv
    def stat(self, obj):    return obj.status_order
    def date_orders(self,obj):return obj.date_order

    stat.short_description='حالة الطلب'
    ids.short_description = 'اسم الخدمة'
    posi.short_desciption='موقع الخدمة'
    ido.short_description = 'اسم المستفيد'

    date_orders.short_description='تاريخ الطلب'
    list_display=['ido','ids','stat','number_person','date_orders','posi',]
    list_display_links=['ids','ido',]
    list_filter =['idserv']

admin.site.register(orders,AdminOrders)





class AdminAdvertisin(admin.ModelAdmin):
    fields = []
    def get_form(self, request, obj=None, **kwargs):
        form2 = super().get_form(request, obj, **kwargs)
        form2.base_fields["title"].label = "العنوان"
        form2.base_fields["details"].label = "التفاصيل"
        form2.base_fields["photo"].label = " الصور"
        return form2;
admin.site.register(Advertising, AdminAdvertisin)

from .models import Notify
class NotifyAdmin(admin.ModelAdmin):
    list_display = ('notify_detail','read_by_user')
admin.site.register(Notify,NotifyAdmin)

class NotifUserStatusAdmin(admin.ModelAdmin):
    list_display = ('notif','user','status')
admin.site.register(models.NotifUserStatus, NotifUserStatusAdmin)
class NotifAddAdmin(admin.ModelAdmin):
 #inlines = [OrdersInline]
 pass
admin.site.register(models.notif_addnew,NotifAddAdmin)

def my_custom_view(request):
    return HttpResponse('Admin Custom View')