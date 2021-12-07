from StudentResult.student import Students5
from StudentResult.teacher import Teachers6
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
     return render(request,"home.html")
def logout(request):
     return render(request,"logout.html")
def contact(request):
     return render(request,"contact.html")
def result(request):
     return render(request,"result.html")
def about(request):
     return render(request,"about.html")
def add(request):
     return render(request,"add.html")
def login(request):
     return render(request,"login.html")
def register(request):
     return render(request,"home.html")
def show(request):
     std2=Students5.objects.all()
     return render(request,"show.html",{"rows":std2})
def delete(request):
     return render(request,"delete.html")
def update(request):
        return render(request,"update.html")
def forget(request):
        return render(request,"forget.html")
def add2(request):
     a=request.POST["enroll"]
     b=request.POST["name"]
     c=request.POST["course"]
     d=request.POST["branch"]
     e=request.POST["section"]
     f=request.POST["semester"]
     g=request.POST["toc"]
     h=request.POST["dbms"]
     i=request.POST["departmentalelectives"]
     j=request.POST["openelectives"]
     k=int(g)+int(h)+int(i)+int(j)
     l=int(k) / 4
     
    
     
     
     std=Students5(enroll=a,name=b,course=c,branch=d,section=e,semester=f,toc=g,dbms=h,departmentalelectives=i,openelectives=j,totalmarks=k,percentage=l)
     std.save()
     messages.success(request,"record is added successfully")
     return show(request)
     
def deleted(request):
     a=request.POST["enroll"]
     std3=Students5.objects.filter(enroll=a)
     std3.delete()
     messages.success(request,"record is deleted successfully")
     return show(request)
def updated(request):
        a=request.POST["enroll"]
        b=request.POST["name"]
        c=request.POST["course"]
        d=request.POST["branch"]
        e=request.POST["section"]
        f=request.POST["semester"]
        g=request.POST["toc"]
        h=request.POST["dbms"]
        i=request.POST["departmentalelectives"]
        j=request.POST["openelectives"]
        k=int(g)+int(h)+int(i)+int(j)
        l=int(k) / 4
        
        

        std4=Students5.objects.get(enroll=a)
        std4.name=b
        std4.course=c
        std4.branch=d
        std4.section=e
        std4.semester=f
        std4.toc=g
        std4.dbms=h
        std4.departmentalelectives=i
        std4.openelectives=j
        std4.totalmarks=k
        std4.percentage=l
        
        
        std4.save()
        messages.success(request,"record is updated successfully")
        return show(request)
def logined(request):
        a=request.POST["username"]
        b=request.POST["password"]
        
        std5=Teachers6.objects.filter(username=a,psw=b)
        if(len(std5)>=1):
           messages.success(request,"Logined Successfully")
           return render(request,"result.html")
        else:
           messages.error(request,"Invalid User id & password")
           return render(request,"login.html")
def registered(request):
       a=request.POST["username"]
       b=request.POST["fullname"]
       e=request.POST["password"]
       f=request.POST["psw-repeat"]
       g=request.POST["designation"]
       i=request.POST["gender"]
       j=request.POST["phone"]
       l=request.POST["address"]
       m=request.POST["email"]
       n=request.POST["question"]
       o=request.POST["answer"]
       std6=Teachers6(username=a,fullname=b,psw=e,pswrepeat=f,designation=g,gender=i,phone=j,address=l,email=m,question=n,answer=o)
       std6.save()
       messages.success(request,"Registered successfully")
       return render(request,"login.html")
       return show(request)
def forget2(request):
        a=request.POST["username"]
        std7=Teachers6.objects.filter(username=a)
        return render(request,"security.html",{"std7":std7[0]})
def editpassword(request):
        return render(request,"changepassword.html")
def editpassword2(request):
        a=request.POST["username"]
        b=request.POST["oldpassword"]
        c=request.POST["newpassword"]
        std10=Teachers6.objects.get(username=a,psw=b)
        std10.psw=c
        std10.save()
        return render(request,"login.html")
def forgetpass2(request):
       a=request.POST["question"]
       b=request.POST["answer"]
       c=request.POST["username"]
       std9=Teachers6.objects.filter(username=c,answer=b)
       if (len(std9)>=1):
            return HttpResponse(std9[0].psw)
       else:
            return HttpResponse("Not Found")

             
