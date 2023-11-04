from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []





def Home(request):
    return render(request,'app1/index.html')

def Auser(request):
    return render(request,'app1/user.html')
def Flip(request):
    return render(request,'app1/Flipcard.html')

def Tour(request):
    return render(request,'app1/Tour.html')

def Dis(request):
    return render(request,'app1/display.html')

def Deposite(request):
    if request.method=='POST':
        am=request.POST.get('am')
        a=int(am)
        amt=a/4

        id=1
        while id<=4:
            user1=User.objects.get(pk=id)
            amv=user1.Amount
            #print(amv)
            act=amv-amt
            #print(act)
            # Amount=act
            user1.Amount=act
            # u=user1(Amount=act)
            user1.save()
            print(act)
            print(user1.Amount)
            # user1.Amount.save()
            # anc=user1.Amount
            # anc.save()
            # print(anc)
            id+=1
        return render(request,'app1/index.html')
    return render(request,'index.html')
#========================================================================================
def Flipcard(request):
    if request.method=='POST':
        am=request.POST.get('am')
        a=int(am)
        id=1
        while id<=4:
            user1=User.objects.get(pk=id)
            amv=user1.Amount
        
            print(amv)
            if (id==2):
                ard=int(a/3.8)
                print(ard)
                ab=amv-ard
                user1.Amount=ab
                user1.save()
                print(user1.Amount)
            if(id==3):
                ard=int(a/1.42)
                ab=amv-ard
                user1.Amount=ab
                user1.save()
            
            id+=1
        return render(request,'app1/index.html')
    #=====================================================================================
def Tour1(request):
    if request.method=='POST':
        am=request.POST.get('am')
        a=int(am)
        id=1
        while id<=4:
            user1=User.objects.get(pk=id)
            amv=user1.Amount
            if id==1:
                act=a*40/100
                amt=amv-act
                user1.Amount=amt
                user1.save()
            if id==2:
                act=a*20/100
                amt=amv-act
                user1.Amount=amt
                user1.save()
            if id==3:
                act=a*20/100
                amt=amv-act
                user1.Amount=amt
                user1.save()
            if id==4:
                act=a*20/100
                amt=amv-act
                user1.Amount=amt
                user1.save()

            id+=1
        return render(request,'app1/index.html')
    
def Display(request):
    data=User.objects.all()
    return render(request,'app1/display.html',{'data':data})




