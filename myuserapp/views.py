from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . models import Student
from . models import Category, Product
# Create your views here.

def mailsenddemo(request):
    subject = 'Django Mail Demo'
    message = 'Hello How are you ?'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['hetvikrishn@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")

def homepageview(request):
    return render (request,'home.html')

def aboutpageview(request):
    return render (request,'about.html')

def contactpageview(request):
    return render (request,'contact.html')

def shoppage(request):
    return render (request,'shop.html')

def saveSessionData(request):
    request.session['username'] = "Hetvi Patel"
    return HttpResponse ("Session Created")

def getSessionData(request):
   if request.session.has_key('username'):
    msg = request.session['username'] 
    return HttpResponse (msg)
   else:
       return HttpResponse ("Session Variable not Present")

def deleteSessionData(request):
    del request.session['username']
    return HttpResponse ("Session Removed")

def getSessionData2(request):
    msg = request.session['username'] 
    return HttpResponse(msg)
   
def contactprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    mymsg = "Hello has Contact you", txt1," Mobile No is ",txt2," Message is ",txt3
    subject = 'Contact us From Website'
    email_from = settings.EMAIL_HOST_USER
    message = mymsg
    recipient_list = ['hetvikrishn@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Thank you for Contacting us.")


def loginpage(request):
    subject = 'Welcome to Origin'
    message = 'Your are selected as CEO'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['hetvikrishn@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'login.html')


def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)
    
def logout(request):
    del request.session['myemail']
    return redirect(loginpage)

def addstudentform(request):
    return render(request,'add-student.html')

def addstudentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    Student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    mymsg = "Hello has signup", txt1," Mobile No is ",txt2," Email is ",txt3, " Address is ",txt4
    subject = 'Contact us From Website'
    email_from = settings.EMAIL_HOST_USER
    message = mymsg
    recipient_list = ['hetvikrishn@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Thank you for Signup")

def displayStudent(request):
    mystudentlist = Student.objects.all()
    return render(request,'display-student.html',{'mydata':mystudentlist})

def deleteStudent(request,id):
    Student.objects.get(id=id).delete()
    return redirect(displayStudent)

def add_category(request):
    if request.method == "POST":
        txt1 = request.POST['txt1']
        Category.objects.create(title=txt1)
        return redirect('add_category')
    return render(request,'add-category.html')

def display_category(request):
    categorylist = Category.objects.all()
    return render(request, 'display-category.html',{'category': categorylist})

def delete_category(request,id):
    Category.objects.get(id=id).delete()
    return redirect('display_category')

def edit_category(request,id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.title = request.POST['txt1']
        category.save()
        return redirect('display_category')
    return render(request, 'edit-category.html', {'category': category})