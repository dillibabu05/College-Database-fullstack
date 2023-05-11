from django.http import request
from django.shortcuts import render,HttpResponse
#table import
#messages import
from django.contrib import messages

# from . models import admission_table
from . models import *

from django.conf import settings
from django.core.mail import send_mail

import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
#login_form_submission
def login_form_submisson(request):
    if request.method=='POST':
        if register_table.objects.filter(user_name=request.POST.get('user_name'),password=request.POST.get('password')):
            print('login successfully')
            logger_data=register_table.objects.get(user_name=request.POST.get('user_name'),password=request.POST.get('password'))
            return render(request,"index_dashboard.html",{'logger_data':logger_data})
        else:
            print("failed to login")
            messages.error(request,'invalid username and password',extra_tags='invalid')
            return render(request,'login.html')

def register(request):
    return render(request,'register.html')
#register_form_submission
def register_form_submission(request):
    if request.method=='POST':
        if register_table.objects.filter(user_name=request.POST.get('user_name')):
             print("already this user name has taken...")
             messages.error(request,'already this user name has taken...',extra_tags='already')
             return render(request,'register.html')
        else:
            reg=register_table(user_name=request.POST.get('user_name'),
                               password=request.POST.get('password'),
                               email_id=request.POST.get('email_id'))
            if len(request.FILES) != 0:
                reg.profile_picture = request.FILES.get('profile_picture')
            
            reg.save()
            #api code
            
            try:
                otp_number=random.randint(000000,999999)
                print(f"your otp number is :",otp_number)
                
                email_id=request.POST.get('email_id')

                print(f"user email is {email_id}")
                subject = 'welcome to BTREE'
                   
                message = f'Hi {email_id}, thank you for registering in BTREE your otp number is {otp_number}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email_id, ]
                send_mail( subject, message, email_from, recipient_list )
                print("mail sent successfuly")
        
                return render(request,'login.html')
            except:
                print("********sorry email is not sending please type proper email id")
                return render(request,'login.html')
    else:
        print("sorry not connected")
        return render(request,'register.html')
        

def index_dashboard(request):
    return render(request,'index_dashboard.html')

def tables_bootstrap(request,id):
    logger_data=register_table.objects.get(id=id)
    view_data=admission_table.objects.all()
    return render(request,'tables_bootstrap.html',{'logger_data':logger_data,'view_data':view_data})
  
def profile(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'profile.html',{'logger_data':logger_data})

def icons_feather(request):
    return render(request,'icons_feather.html')

def aditamissionadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'aditamissionadd.html',{'logger_data':logger_data})

def editpage(request,id,row_id):
    logger_data=register_table.objects.get(id=id)
    get_data=admission_table.objects.get(id=row_id)
    return render(request,'editpage.html',{'logger_data':logger_data,'get_data':get_data})

def visitorbook(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'visitorbook.html',{'logger_data':logger_data})

def addvisitor(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'addvisitor.html',{'logger_data':logger_data})

def editvisitor(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'editvisitor.html',{'logger_data':logger_data})

def studentview(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentview.html',{'logger_data':logger_data})

def studentviewadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentviewadd.html',{'logger_data':logger_data})

def studentviiewedit(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentviiewedit.html',{'logger_data':logger_data})

def studentadmision(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentadmision.html',{'logger_data':logger_data})

def studentadmissionadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentadmissionadd.html',{'logger_data':logger_data})

#admission form submission code
def admission_form_submission(request,id):
    if request.method=='POST':
        ex1=admission_table(name=request.POST.get('name'),
                          date=request.POST.get('date'),
                          email=request.POST.get('email'),
                          course=request.POST.get('course'))
        ex1.save()
        print("saved successfully")
        logger_data=register_table.objects.get(id=id)
        messages.error(request,"data added successfully",extra_tags='added')
        view_data=admission_table.objects.all()
        return render(request,'tables_bootstrap.html',{'view_data':view_data,'logger_data':logger_data})

#update_form
def admission_update_form_submission(request,id,row_id):

    ex1=admission_table.objects.filter(id=row_id).update(name=request.POST.get('name'),
                                                     
                                                      email=request.POST.get('email'),
                                                     )
    messages.error(request,'data updated succssully',extra_tags='data')
    logger_data=register_table.objects.get(id=id)
    view_data=admission_table.objects.all()
    return render(request,'tables_bootstrap.html',{'logger_data':logger_data,'view_data':view_data})

#delete_form
def delete_admission_form(request,id,row_id):
    ex1=admission_table.objects.get(id=row_id)
    ex1.delete()
    messages.error(request,'data deleted succssully',extra_tags='data')
    print("data deleted successfully...")
    #star_code
    logger_data=register_table.objects.get(id=id)
    view_data=admission_table.objects.all()
    return render(request,'tables_bootstrap.html',{'logger_data':logger_data,'view_data':view_data})

def studentadmisionedit(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentadmisionedit.html',{'logger_data':logger_data})

def onlineadmission(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'onlineadmission.html',{'logger_data':logger_data})

def onlineadmissionadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'onlineadmissionadd.html',{'logger_data':logger_data})

def onlineadmissioneit(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'onlineadmissioneit.html',{'logger_data':logger_data})

def feesdetails(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'feesdetails.html',{'logger_data':logger_data})

def feesdetailsadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'feesdetailsadd.html',{'logger_data':logger_data})

def feesdetailsedit(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'feesdetailsedit.html',{'logger_data':logger_data})

def stufeescollect(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'stufeescollect.html',{'logger_data':logger_data})

def stufeescollectadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'stufeescollectadd.html',{'logger_data':logger_data})

def stufeescollectedit(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'stufeescollectedit.html',{'logger_data':logger_data})

def feesdiscount(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'feesdiscount.html',{'logger_data':logger_data})

def adddiscount(request):
    return render(request,'adddiscount.html')

def editfeesdiscount(request):
    return render(request,'editfeesdiscount.html')

def incomedetails(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'incomedetails.html',{'logger_data':logger_data})

def addincome(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'addincome.html',{'logger_data':logger_data})

def editincome(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'editincome.html',{'logger_data':logger_data})

def expensesdetails(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'expensesdetails.html',{'logger_data':logger_data})

def addexpenses(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'addexpenses.html',{'logger_data':logger_data})

def editexpense(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'editexpense.html',{'logger_data':logger_data})

def studentattendence(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentattendence.html',{'logger_data':logger_data})

def addleavebutton(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'addleavebutton.html',{'logger_data':logger_data})

def editleavebutton(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'editleavebutton.html',{'logger_data':logger_data})

def studentapprove(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentapprove.html',{'logger_data':logger_data})

def studentapproveadd(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentapproveadd.html',{'logger_data':logger_data})

def studentapproveedit(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request,'studentapproveedit.html',{'logger_data':logger_data})

def Examgroup(request):
    return render(request,'Examgroup.html')

def examaddpage(request):
    return render(request,'examaddpage.html')

def examiconedit(request):
    return render(request,'examiconedit.html')

def examlistpage(request):
    return render(request,'examlistpage.html')

def exlistaddbu(request):
    return render(request,'exlistaddbu.html')

def exlisticonadd(request):
    return render(request,'exlisticonadd.html')

def exschedulelist(request):
    return render(request,'exschedulelist.html')

def examschedadd(request):
    return render(request,'examschedadd.html')

def examschededit(request):
    return render(request,'examschededit.html')

def Examresult(request):
    return render(request,'Examresult.html')

def examresultadd(request):
    return render(request,'examresultadd.html')

def examresultedit(request):
    return render(request,'examresultedit.html')

def onlineexamsch(request):
    return render(request,'onlineexamsch.html')

def onlineexamschadd(request):
    return render(request,'onlineexamschadd.html')

def onlineexshledit(request):
    return render(request,'onlineexshledit.html')

def onlinesemexamfile(request):
    return render(request,'onlinesemexamfile.html')

def onlinesemfileadd(request):
    return render(request,'onlinesemfileadd.html')

def onlinsemexamedit(request):
    return render(request,'onlinsemexamedit.html')

def classtimetable(request):
    return render(request,'classtimetable.html')

def classtimetableadd(request):
    return render(request, 'classtimetableadd.html')

def classtimetableedit(request):
    return render(request, 'classtimetableedit.html')

def teachertimetable(request):
    return render(request, 'teachertimetable.html')

def teachertietableadd(request):
    return render(request, 'teachertietableadd.html')

def teachertimetableedit(request):
    return render(request, 'teachertimetableedit.html')

def subjectlist(request):
    return render(request, 'subjectlist.html')

def subjectlistadd(request):
    return render(request, 'subjectlistadd.html')

def subjectlistedit(request):
    return render(request, 'subjectlistedit.html')

def staffdirtlist(request):
    return render(request, 'staffdirtlist.html')

def staffdirtlistadd(request):
    return render(request, 'staffdirtlistadd.html')

def staffdirtlistedit(request):
    # logger_data=register_table.objects.get(id=id)
    return render(request, 'staffdirtlistedit.html')

def staffattencelist(request):
    # logger_data=register_table.objects.get(id=id)
    return render(request, 'staffattencelist.html')

def staffattenceadd(request):
    # logger_data=register_table.objects.get(id=id)
    return render(request, 'staffattenceadd.html')

def staffattenceedit(request):
    return render(request, 'staffattenceedit.html')

def satffleaveform(request):
    return render(request, 'satffleaveform.html')

def satffleaveadd(request):
    return render(request, 'satffleaveadd.html')

def satffleaveaedit(request):
    return render(request, 'satffleaveaedit.html')

def librarybooklist(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request, 'librarybooklist.html',{'logger_data':logger_data})

def addbookpage(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request, 'addbookpage.html',{'logger_data':logger_data})

def editbookpage(request,id):
    logger_data=register_table.objects.get(id=id)
    return render(request, 'editbookpage.html',{'logger_data':logger_data})

def googlemeettimetable(request):
    return render(request, 'googlemeettimetable.html')

def googlemeettimetableadd(request):
    return render(request, 'googlemeettimetableadd.html')

def googlemettttimetabledit(request):
    return render(request, 'googlemettttimetabledit.html')

def onlineclassdet(request):
    return render(request, 'onlineclassdet.html')

def onlineclassdetadd(request):
    return render(request, 'onlineclassdetadd.html')

def onlineclassdetedit(request):
    return render(request, 'onlineclassdetedit.html')

def downlobonafidecert(request):
    return render(request, 'downlobonafidecert.html')

def downlobonafidecertadd(request):
    return render(request, 'downlobonafidecertadd.html')

def downlobonafidecertedit(request):
    return render(request, 'downlobonafidecertedit.html')

def downloattencecerif(request):
    return render(request, 'downloattencecerif.html')

def downloattencecerifadd(request):
    return render(request, 'downloattencecerif.html')

def downloattencecerifedit(request):
    return render(request, 'downloattencecerif.html')

def studentfeedback(request):
    return render(request, 'studentfeedback.html')

def studentfeedbackadd(request):
    return render(request, 'studentfeedbackadd.html')

def studentfeedbackedit(request):
    return render(request, 'studentfeedbackedit.html')

def teacherfeedback(request):
    return render(request, 'teacherfeedback.html')

def teacherfeedbackadd(request):
    return render(request, 'teacherfeedbackadd.html')
    
def teacherfeedbackedit(request):
    return render(request, 'teacherfeedbackedit.html')

def contact_form_submission(request):
    ex1=contact_table(name=request.POST.get('name'),
                      email=request.POST.get('email'),
                      phone=request.POST.get('phone'),
                      message=request.POST.get('message'))
    ex1.save()
    return HttpResponse(ex1)

# filter
def search_filter(request):
    view_data=admission_table.objects.filter(name=request.POST.get('name'))
    return render(request,'tables_bootstrap.html',{'view_data':view_data})
