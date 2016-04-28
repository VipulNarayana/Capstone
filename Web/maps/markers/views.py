from django.core.mail import send_mail
from newsletter.models import User

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.shortcuts import render
import csv
from .models import Vehicle
# Create your views here.
import os
from datetime import datetime

def index(request):
    filename = 'C:\\Users\\Harsha Vardhan\\Desktop\\Python\\VehicleCount.csv'
    if os.path.isfile(filename) and os.stat(filename).st_size > 0  :
        with open(filename, 'r') as f :
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row1 in reader:
                if row1:
                    tmp = Vehicle.objects.create()
                    tmp.vehicle = row1[0]
                    tmp.flag = row1[1]
                    tmp.time = row1[2]
                    tmp.count = row1[3]
                    tmp.save()

                    for row in Vehicle.objects.all() :
                        if row.count < int(tmp.count) :
                            row.flag = 1
                            row.save()

                    a = Vehicle.objects.values_list('time', flat=True)
                    b = list(set(a))
                    for unq in range(0,len(b)):
                        count = 0
                        for row in Vehicle.objects.all():
                            if b[unq] == row.time :
                                count = count + 1
                                if count > 1 :
                                    row.delete()
                
    else :
        Vehicle.objects.all().delete()
        veh_all=Vehicle.objects.all()
        context={'veh_all':veh_all}
        return render(request,'markers/index.html',context)
        
   

    a = Vehicle.objects.all()
    count = 0
    FMT = '%H:%M:%S'
    
    for row in a :
        
        b = str(a[0].time)
        c = str(row.time)
        tdelta = datetime.strptime(b, FMT) - datetime.strptime(c, FMT)
        
        if  tdelta.total_seconds() < 300 :
            count = count+1;
        


    veh_all=Vehicle.objects.all()
   
    
    if count > 3 :
        trafficInt = 'High'
    else :
        trafficInt = 'Low'

    if trafficInt == 'High' :
        subject='Traffic Updates at VIT University'
        from_mail='mnvipul@gmail.com'
        to_mail=User.objects.values_list('email',flat=True)
        html_content=render_to_string('markers/testmail.html',{'trafficInt':trafficInt,'count':count})
        text_content=strip_tags(html_content)
        msg=EmailMultiAlternatives(subject,text_content,from_mail,to_mail)
        msg.attach_alternative(html_content,'text/html')
        msg.send()
        
    context={'veh_all':veh_all,
             'totcount':count,
             }     
    return render(request,'markers/index.html',context)

