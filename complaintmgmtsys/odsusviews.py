from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required

from cmsapp.models import CustomUser,UserReg,Category,Subcategory,Complaints,ComplaintRemark, Categorycitymup, Subcategorycitymup, PacdComplaints, PacdComplaintRemark,Odsus, OdsusRemark
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import random




@login_required(login_url='/')
def ODSUSHOME(request):
    user_admin = request.user

    # Get the user's registration details
    try:
        user_reg = UserReg.objects.get(admin=user_admin)
    except UserReg.DoesNotExist:
        return render(request, 'odsus/odsusdashboard.html', {'error': 'No user registration found.'})

    # Get the user's assigned division (Category) and section (Subcategory)
    user_division = user_reg.cat  # Division (Category)
    user_section = user_reg.subcategory  # Section (Subcategory)

    # Retrieve only complaints related to the user's division and section
    complaints = Complaints.objects.filter(cat_id=user_division, subcategory_id=user_section).order_by('-complaintdate_at')

    # Pagination
    paginator = Paginator(complaints, 10)  # Show 10 complaints per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Count complaints only related to the user's division and section
    complaints_count = complaints.count()
    newcom_count = complaints.filter(status='0').count()
    ipcom_count = complaints.filter(status='Inprocess').count()
    resolved_count = complaints.filter(status='Resolved').count()
    closed_count = complaints.filter(status='Closed').count()

    # Directory complaint count based on prefixes in `complaint_text`
    dir_complaint_count = complaints.filter(complaint_text__startswith="CARAGA-FO-ROC-DIR-25-").count()
    dir_complaint_count2 = complaints.filter(complaint_text__startswith="CARAGA-FO-ROC-INQ-25-").count()
    dir_complaint_count3 = complaints.filter(complaint_text__startswith="CARAGA-FO-ROC-PACE-25-").count()
    dir_complaint_count4 = complaints.filter(complaint_text__startswith="CARAGA-FO-ROC-CSCCCB-25-").count()

    context = {
        'page_obj': page_obj,  # Updated to use paginated object
        'complaints_count': complaints_count,
        'newcom_count': newcom_count,
        'ipcom_count': ipcom_count,
        'resolved_count': resolved_count,
        'closed_count': closed_count,
        'dir_complaint_count': dir_complaint_count,
        'dir_complaint_count2': dir_complaint_count2,
        'dir_complaint_count3': dir_complaint_count3,
        'dir_complaint_count4': dir_complaint_count4,
    }

    return render(request, 'odsus/odsusdashboard.html', context)









def ODSUSSIGNUP(request):
   
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
            return redirect('odsussignup')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist')
            return redirect('odsussignup')
        else:
            user = CustomUser(
               first_name=first_name,
               last_name=last_name,
               username=username,
               email=email,
               user_type=4,
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
    
    

    return render(request,'odsus/odsus_reg.html')


#PACDEVEREG REGISTRATION
@login_required(login_url='/')
def ODSUSREG(request):
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
            complaint_text = f"CARAGA-FO-ROC-ODSUS-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Odsus(
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

    return render(request, 'odsus/register-odsusevereg.html', context)




@login_required(login_url='/')
def ODSUSHISTORY(request):
    userreg = request.user.userreg
    complaint_list = Odsus.objects.filter(userregid=userreg).order_by('-complaintdate_at')
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
    return render(request, 'odsus/odsus-history.html', context)


@login_required(login_url='/')
def ODSUSHISTORYDETAILS(request, id):
    complaints = Complaints.objects.get(id=id)
    complaintsremarks = ComplaintRemark.objects.filter(comp_id_id=id)
      
    context = {
         'complaints':complaints,
         'complaintsremarks':complaintsremarks,
    }
    return render(request,'user/complaint-details.html',context)