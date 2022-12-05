from django import urls
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.conf import settings
from qrcode import *
import time
from .models import DeviceManagmentService
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


#-------------start register---------------#
def signInView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("error")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def signoutView(request):
    logout(request)
    return redirect('login')
#-------------end register---------------#


#---------------start qr code------------#
@login_required
def qr_gen(request):
    if request.method == 'POST':
        data1 = request.POST['site_name']
        data2 = request.POST['site_type']
        data3 = request.POST['serial_number']        

        #saving data to database
        img_name = 'qr' + str(time.time()) + '.png'
        store_data = DeviceManagmentService(site_name=data1, site_type=data2, serial_number=data3, qr=img_name)    
        store_data.save()
        
        #---------------------you have to edit the link after you upload the webiste-------------------------#
        data = "http://127.0.0.1:8000/siteDetail/" + str(store_data.id)
        #----------------------------------------------------------#
        
        img = make(data)
        
        img.save(settings.MEDIA_ROOT + '/' + img_name)
        messages.success(request, "Qr code Generated.")
    
        return render(request, 'qrGenerator.html', {'img_name': img_name})

    return render(request, 'qrGenerator.html')


#--------------end qr code------------------#



#-----------------start getting data from database-------#
@login_required
def dashboard(request):
    data = DeviceManagmentService.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(data, 15)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request, 'dashboard.html', {'data': data})


def siteDetail(request, id):
    detail = DeviceManagmentService.objects.filter(id=id)
    return render(request, 'siteDetail.html', {'detail': detail})
    

#-----------------end getting data from database-------#



## search
@login_required
def searchResult(request):
    posts = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        posts = DeviceManagmentService.objects.all().filter(Q(site_name__contains=query) |
                                            Q(site_type__contains=query) |
                                            Q(serial_number__contains=query))
    
    return render(request, 'search.html', {'query': query, 'data': posts})
## end search
