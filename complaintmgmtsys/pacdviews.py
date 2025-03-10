from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

from cmsapp.models import CustomUser,UserReg,Category, Categorycitymup, Subcategorycitymup, PacdComplaints, PacdComplaintRemark
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import random




@login_required(login_url='/')
def PACDUSERHOME(request):
    user_admin = request.user
    user_reg = UserReg.objects.get(admin=user_admin)
    complaints = PacdComplaints.objects.all().order_by('remind_date')
    complaints_count = PacdComplaints.objects.filter(userregid=user_reg).count()
    newcom_count = PacdComplaints.objects.filter(status='0',userregid=user_reg).count()
    ipcom_count = PacdComplaints.objects.filter(status='Inprocess',userregid=user_reg).count()
    closed_count = PacdComplaints.objects.filter(status='Closed',userregid=user_reg).count()
    context = {
    'complaints':complaints,
    'complaints_count':complaints_count,
    'newcom_count':newcom_count,
    'ipcom_count':ipcom_count,
    'closed_count':closed_count,        
    }
    return render(request,'pacd/pacduserdashboard.html',context)

def PACDUSERSIGNUP(request):
   
    if request.method == "POST":
        pic = request.FILES.get('pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')        
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email already exist')
            return redirect('pacdusersignup')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist')
            return redirect('pacdusersignup')
        else:
            user = CustomUser(
               first_name=first_name,
               last_name=last_name,
               username=username,
               email=email,
               user_type=3,
               profile_pic = pic,
            )
            user.set_password(password)
            user.save()            
            comuser = UserReg(
                admin = user,                
                mobilenumber = mobno,              
                
            )
            comuser.save()            
            messages.success(request,'Signup Successfully')
            return redirect('login')
    
    

    return render(request,'pacd/pacduser_reg.html')


#PACDEVEREG REGISTRATION
@login_required(login_url='/')
def PACDEVEREG(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()

    if request.method == "POST":
        try:
            # Fetching data from the form
            cat_id = request.POST.get('cat_id')
            subcategory_id = request.POST.get('subcategory_id')
            deadline = request.POST.get('deadline')
            passed_date = request.POST.get('passed_date')
            date_received = request.POST.get('date_received')
            date_endorse = request.POST.get('date_endorse')
            remind_date = request.POST.get('remind_date')
            time_received = request.POST.get('time_received')
            time_acknowledge = request.POST.get('time_acknowledge')
            time_endorse = request.POST.get('time_endorse')
            region_name = request.POST.get('region_name', 'Unknown')
            province_name = request.POST.get('province_name', 'Unknown')
            city_name = request.POST.get('city_name', 'Unknown')
            barangay_name = request.POST.get('barangay_name', 'Unknown')
            selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
            complaint_email = request.POST.get('complaint_email', '')
            complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
            endorseemp  = request.POST.get('endorseemp', 'Unknown')
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            clientdetails = request.POST.get('clientdetails')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Generating a unique complaint number
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"CARAGA-FO-ROC-PACD-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = PacdComplaints(
                cat_id_id=cat_id,
                subcategory_id_id=subcategory_id,
                deadline=deadline,
                region_name=region_name,
                province_name=province_name,
                city_name=city_name,
                barangay_name=barangay_name,
                passed_date=passed_date,
                remind_date=remind_date,
                date_endorse=date_endorse,
                date_received=date_received,
                time_received=time_received,
                time_endorse=time_endorse,
                time_acknowledge=time_acknowledge,
                complaint_text=complaint_text,
                complainant_fname=complainant_fname,
                complainant_pace=complainant_pace,
                complaint_email=complaint_email,
                selfcomplaint_number=selfcomplaint_number,
                complainttype=complainttype,
                clientdetails = clientdetails,
                noc=noc,
                endorseemp=endorseemp,
                complaindetails=complaindetails,
                compfile=compfile,
                userregid=userreg,
            )
            complaint.save()

            messages.success(request, 'Complaint Lodged Successfully!')
            return redirect("pacdevereg")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
    }

    return render(request, 'pacd/register-pacdevereg.html', context)




@login_required(login_url='/')
def PACDCOMPLAINTHISTORY(request):
    userreg = request.user.userreg
    complaint_list = PacdComplaints.objects.filter(userregid=userreg).order_by('-complaintdate_at')
    paginator = Paginator(complaint_list, 10)  # Show 10 complaints per page

    page_number = request.GET.get('page')
    try:
        complaints = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        complaints = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        complaints = paginator.page(paginator.num_pages)

    context = {'complaints': complaints}
    return render(request, 'pacd/pacdcomplaint-history.html', context)


@login_required(login_url='/')
def PACDCOMPLAINTHISTORYDETAILS(request,id):
    complaints = PacdComplaints.objects.get(id=id)
    complaintsremarks = PacdComplaintRemark.objects.filter(comp_id_id=id)
      
    context = {
         'complaints':complaints,
         'complaintsremarks':complaintsremarks,
    }
    return render(request,'pacd/pacdcomplaint-details.html',context)