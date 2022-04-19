from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse, request
from django import template
from django.shortcuts import render
from services.models import person,orders,services
import os

from .models import Image
from  django.contrib import messages
from dbr import *
import json
import cv2
from pyzbar import pyzbar
from  pyzbar.pyzbar import decode

# كود يقرأء الباركود من صورة وليس من الكاميرا
 #im=cv2.imread('new code1111.png')
#for code in decode(im):
 #   print(code.type)
  #  print(code.data.decode('utf-8'))
# كود يقرأ من الكاميرا لكن لم أستخدمه
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        # 3
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame
def main1():


    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
    #4
    if __name__ == '__main1__':
       main1()


reader = BarcodeReader()

# Apply for a trial license: https://www.dynamsoft.com/customer/license/trialLicense?product=dbr
reader.init_license("LICENSE-KEY")

def index(request):
 # main1()

 #هنا من أجل قرأءة الباركود من الكاميرا
  per=None
  xxxx=None
  context={}
  cap=cv2.VideoCapture(0)
  cap.set(3,640)
  cap.set(4,480)
  camera =True



  while camera ==True:
      success,frame= cap.read()
      cv2.imshow('testing', frame)
      cv2.waitKey(1)

      for code in decode(frame):
          x=1
          code_type= code.type
          code_data= code.data.decode('utf-8')
          print(code_data)
          xxxx=code_data
          per = person.objects.filter(barcode=xxxx)
          if per.exists():
             order = orders.objects.filter(idperson=per[0])
             if per is not None:
                 context = {'per': per,
                            'order': order,
                            # 'ser':ser
                            }

                 cv2.destroyAllWindows()
                 # return render(request, '/admin/services/person/' + str(per[0]), context)هذه الطريقة لم تعمل
                 return render(request, 'scanbarcode/index.html', context)
          else:
              cv2.destroyAllWindows()
              messages.error(request, 'المستفيد ليس موجود ')
              return  render(request,'part/success.html')
         # ser = services.objects.all()


              #filter(idperson=per )





             # break
              #cv2.destroyAllWindows()


     # per = person.objects.filter(barcode=xxxx)
      #context={'per':per}
      #camera=False
             # redirect( to='services/index.html')
          #print(code.type)
          #print(code.data.decode('utf-8'))

     # if person.objects.filter(barcode=xxxx).exists():
      #    per = person.objects.filter(barcode=xxxx)
       #   context={'per':per}
        #  return render(request, 'scanbarcode/index.html', context)

  return render(request, 'scanbarcode/index.html',context)

#def upload(request):
 #   out = "No barcode found"
  #  if request.method == 'POST':
   #     filePath = handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
    #    try:
     #       text_results = reader.decode_file(filePath)
      #      if text_results != None:
       #         out = ''
        #        for text_result in text_results:
         #           out += "Barcode Format : " + text_result.barcode_format_string + "\n"
          #          out += "Barcode Text : " + text_result.barcode_text + "\n"
           #         out += "------------------------------------------------------------\n"
        #except BarcodeReaderError as bre:
         #   print(bre)
          #  return HttpResponse(out)


        #return HttpResponse(out)
        #image = Image()
        #image.name = request.FILES['RemoteFile'].name
        #image.data = request.FILES['RemoteFile']
        #image.save()
        #return HttpResponse("Successful")

    #return HttpResponse(out)

#def handle_uploaded_file(file, filename):
 #   if not os.path.exists('upload/'):
  #      os.mkdir('upload/')

   # filePath = 'upload/' + filename
    #with open(filePath, 'wb+') as destination:
     #   for chunk in file.chunks():
      #      destination.write(chunk)

       # return filePath




