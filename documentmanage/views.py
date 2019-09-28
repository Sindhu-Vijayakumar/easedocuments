from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from documentmanage.models import AllDocuments,Requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        exists = User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            return redirect("/student/")
        else:
            return render(request, "signup.html",{"error":"User already exists"})
    
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("/manager/")
            return redirect("/student/")
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, "signin.html")

@login_required(login_url="/login")
def signout(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login")
def student(request):
    if request.user.is_staff:
        return redirect("/manager/")
    Documentdetails ={}
    AllDoc = AllDocuments.objects.all()
    for eachdocument in AllDoc:
        exists = Requests.objects.filter(user=request.user,document=eachdocument).exists()
        Documentdetails[eachdocument]=exists
    print(Documentdetails)
    return render(request, "student.html",{"documentdetails":Documentdetails})

@login_required(login_url="/login")
def send_request(request):
    if request.method == "POST":
        docname = request.POST["docname"]
        addinfo = request.POST["addinfo"]
        document=AllDocuments.objects.get(docname=docname)
        new_request = Requests.objects.create(user=request.user,document=document, Additionalinfo=addinfo)
        return redirect("/student/")
    
    return redirect("/student/")

@login_required(login_url="/login")
def manager(request):
    if not request.user.is_staff:
        return redirect("/student/")
    ActiveDocs = AllDocuments.objects.all()
    requestedDocs = Requests.objects.all()
    return render(request, "manager.html",{"ActiveDocs":ActiveDocs,"requestedDocs":requestedDocs})

@login_required(login_url="/login")
def deleterequest(request,reqid):
    requested = Requests.objects.get(id=reqid)
    # send_mail(subject, message, from_email, to_list, fail_silently =True)
    subject = requested.document.docname+' document is ready.'
    message = 'Your requested document '+requested.document.docname+' is ready. Please collect it soon. Thanks, EaseDocuments'
    from_email = settings.EMAIL_HOST_USER
    to_list = [requested.user.email,settings.EMAIL_HOST_USER]

    send_mail(subject, message, from_email, to_list, fail_silently =True)
    
    requested.delete()
    return redirect("/manager/")

@login_required(login_url="/login")
def adddocument(request):
    if request.method == "POST":
        docname = request.POST["docname"]
        description = request.POST["description"]
        new_doc = AllDocuments.objects.create(docname=docname, description=description)
        return redirect("/manager/")

def deletedocument(request,deleteid):
    deleterequest = AllDocuments.objects.get(id=deleteid)
    deleterequest.delete()
    return redirect("/manager/")

# def deletedocument()
# create history table
# 

