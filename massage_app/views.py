from django.shortcuts import render,HttpResponse
from .models import mass

# Create your views here.
def create(request):
    if request.method=='POST':
        print("request is:",request.method)
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        print(n)
        print(mail)
        print(mob)
        print(msg)
      #  m=msg.objects.create(name=n,email=mail,mobile=mob,msg=massage)
      #  m.save()
       # return redirect('/dashboard')
        return HttpResponse("data fetched successfully")
    else:
        print("request is:",request.method)
        return render(request,'create.html')
"""
def dashboard(request):
    m=msg.objects.all()
    #print(m)
   # return HttpResponse("data fetched")
    context={}
    context[data]=m
    return render(request,'dashboard.html',context)
    {% endcomment %}
    """


