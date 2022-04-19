from django.shortcuts import render
import  folium
import geocoder
# Create your views here.
from  . import  models,views
from .models import Map_location


def map (request):
    new=Map_location.objects.all()
    location=geocoder.osm('homs')
    lat=location.lat

    lng=location.lng
    country=location.country
    m=folium.Map(location=[36,34],zoom_start=7)
   # folium.Marker([20.594,-0.219]).add_to(m)
    #folium.Marker([lat,lng],tooltip='انقر هنا',popup=country).add_to(m)

    for i in new:
        if i.activity_name  == None:
            folium.Marker([i.lat, i.lng], tooltip='', popup=[i.locations_name],
                          icon=folium.Icon(icon='glyphicon-plane', prefix='glyphicon')
                          ).add_to(m)
        else:
            folium.Marker([i.lat, i.lng], tooltip='انقر هنا', popup=[i.activity_name,i.user_count],
                     icon=folium.Icon(icon='glyphicon-plane',prefix='glyphicon')
                      ).add_to(m)


    m=m._repr_html_()
    context={
        'm':m
    }
    return render(request,'map/map.html',context)
