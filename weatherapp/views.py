from django.shortcuts import render
import requests
import datetime

def home(request):
    if request.method=='POST':
       city=request.POST.get('city')
    else:
        city='chennai'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2aede1399631c1fda876659c16d2feac'
    PARAMS={'units':'metric'}

    try:
        data=requests.get(url,PARAMS).json()
        main=data['weather'][0]['main']
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
        humidity=data['main']['humidity']
        day=datetime.date.today()
        
        return render(request,'index.html',{'des':description,'main':main,'icon':icon,'temp':temp,'city':city,'day':day,'humidity':humidity})

    except requests.exceptions.RequestException:
        error="Network or API error occured"
        return render(request,'index.html',{'error':error})
        


# Create your views here.
