from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required

from cmsapp.models import CustomUser,UserReg,Category,Subcategory,Complaints,ComplaintRemark, Categorycitymup, Subcategorycitymup, PacdComplaints,Odsus
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.utils import timezone




@login_required(login_url='/')
def USERHOME(request):
    user_admin = request.user
    user_reg = UserReg.objects.get(admin=user_admin)
    complaints = Complaints.objects.all().order_by('remind_date')
    complaints_count = Complaints.objects.filter(userregid=user_reg).count()
    newcom_count = Complaints.objects.filter(status='0',userregid=user_reg).count()
    ipcom_count = Complaints.objects.filter(status='Inprocess',userregid=user_reg).count()
    resolved_count = Complaints.objects.filter(status='Resolved',userregid=user_reg).count()
    closed_count = Complaints.objects.filter(status='Closed',userregid=user_reg).count()
    dir_complaint_count = Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-DIR-25-",userregid=user_reg).count()
    dir_complaint_count2 = Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-INQ-25-",userregid=user_reg).count()
    dir_complaint_count3 = Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-PACE-25-",userregid=user_reg).count()
    dir_complaint_count4 = Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-CSCCCB-25-",userregid=user_reg).count()
    
    
    context = {
    'complaints':complaints,
    'complaints_count':complaints_count,
    'newcom_count':newcom_count,
    'ipcom_count':ipcom_count,
    'resolved_count':resolved_count,
    'closed_count':closed_count,
    'dir_complaint_count':dir_complaint_count,
    'dir_complaint_count2':dir_complaint_count2,
    'dir_complaint_count3':dir_complaint_count3,
    'dir_complaint_count4':dir_complaint_count4,
    }
    return render(request,'user/userdashboard.html',context)




def USERSIGNUP(request):
    category = Category.objects.all()
    
    if request.method == "POST":
        pic = request.FILES.get('pic')
        cat_id = request.POST.get('cat_id')
        subcategory_id = request.POST.get('subcategory_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')        
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('usersignup')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('usersignup')

        # Get ForeignKey Instances
        category_instance = Category.objects.get(id=cat_id) if cat_id else None
        subcategory_instance = Subcategory.objects.get(id=subcategory_id) if subcategory_id else None

        # Create User
        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            user_type=4, # Change this type for different user types
            profile_pic=pic,
            cat=category_instance,  # ✅ Correct (Stores FK instance)
            subcategory=subcategory_instance  # ✅ Correct (Stores FK instance)
        )
        user.set_password(password)
        user.save()

        # Create UserReg Entry
        comuser = UserReg(
            admin=user,
            mobilenumber=mobno,
            cat_id=category_instance.id if category_instance else None,  # ✅ Pass ID instead of instance
            subcategory_id=subcategory_instance.id if subcategory_instance else None  # ✅ Pass ID instead of instance
        )
        comuser.save()

        messages.success(request, 'Signup Successfully')
        return redirect('login')

    context = {'category': category}
    return render(request, 'user/user_reg.html', context)




@login_required(login_url='/')
def get_subcat(request):
    if request.method == 'GET':
        c_id = request.GET.get('c_id')
        subcat = Subcategory.objects.filter(cat_id=c_id)
        subcat_options = ''
        for subcategory in subcat:
            subcat_options += f'<option value="{subcategory.id}">{subcategory.subcatname}</option>'
        return JsonResponse({'subcat_options': subcat_options})
    


@login_required(login_url='/')
def get_subcats(request):
    if request.method == 'GET':
        # Fetch the province (catmupname_id) from the request
        catmupname_id = request.GET.get('c_ids')

        # Ensure the province ID is valid
        if catmupname_id:
            subcats = Subcategorycitymup.objects.filter(catmupname_id=catmupname_id)
            subcat_options = ''
            for subcategory in subcats:
                subcat_options += f'<option value="{subcategory.id}">{subcategory.subcatcitymupname}</option>'

            # Return the subcategory options as a JSON response
            return JsonResponse({'subcat_options': subcat_options})
        else:
            # Return an empty options string if no province is selected
            return JsonResponse({'subcat_options': ''})




# ROC DIR REGISTRATION
@login_required(login_url='/')
def REGCOMPLAINT(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()
    compusers = UserReg.objects.select_related('admin').all()  # ✅ Fetch all users
    
    print("DEBUG: Users in Dropdown:", compusers)
    
    if request.method == "POST":
        try:
            # ✅ Fetch division from the form
            cat_id = request.POST.get('cat_id')

            # ✅ Get the division category (Promotive Services Division)
            assigned_division = Category.objects.get(id=cat_id)

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
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Generating a unique complaint number
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"CARAGA-FO-ROC-DIR-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # ✅ Ensure complaint is assigned to the selected division
            complaint = Complaints(
                cat_id=assigned_division,  # ✅ Assign correct division
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
                noc=noc,
                complaindetails=complaindetails,
                compfile=compfile,
                userregid=userreg,
            )
            complaint.save()

            messages.success(request, 'Complaint Lodged Successfully!')
            return redirect("regcomplaint")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
        'compusers': compusers,
    }

    return render(request, 'user/register-complaint.html', context)



#ROC PACD REGISTRATION
@login_required(login_url='/')
def PACDOCOMPLAINT(request):
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
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Generating a unique complaint number
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"CARAGA-FO-ROC-PACD-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Complaints(
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
                noc=noc,
                complaindetails=complaindetails,
                compfile=compfile,
                userregid=userreg,
            )
            complaint.save()

            messages.success(request, 'Complaint Lodged Successfully!')
            return redirect("pacdcomplaint")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
    }

    return render(request, 'user/register-complaint-pacd.html', context)


# INQUIRY
@login_required(login_url='/')
def NON8888REGCOMPLAINT(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()
    compusers = UserReg.objects.select_related('admin').all()  # ✅ Fetch all users
    
    print("DEBUG: Users in Dropdown:", compusers)
    
    if request.method == "POST":
        try:
            # ✅ Fetch division from the form
            cat_id = request.POST.get('cat_id')

            # ✅ Get the division category (Promotive Services Division)
            assigned_division = Category.objects.get(id=cat_id)

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
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Generating a unique complaint number
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"CARAGA-FO-ROC-INQ-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # ✅ Ensure complaint is assigned to the selected division
            complaint = Complaints(
                cat_id=assigned_division,  # ✅ Assign correct division
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
                noc=noc,
                complaindetails=complaindetails,
                compfile=compfile,
                userregid=userreg,
            )
            complaint.save()

            messages.success(request, 'Complaint Lodged Successfully!')
            return redirect("regcomplaint")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
        'compusers': compusers,
    }

    return render(request, 'user/register-complaint-non-8888.html', context)


#ROC-PACE REGISTRATION
@login_required(login_url='/')
def PACEREGCOMPLAINT(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()
    compusers = UserReg.objects.select_related('admin').all()  # ✅ Fetch all users
    
    print("DEBUG: Users in Dropdown:", compusers)
    
    if request.method == "POST":
        try:
            # ✅ Fetch division from the form
            cat_id = request.POST.get('cat_id')

            # ✅ Get the division category (Promotive Services Division)
            assigned_division = Category.objects.get(id=cat_id)

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
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Generating a unique complaint number
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"CARAGA-FO-ROC-PACE-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # ✅ Ensure complaint is assigned to the selected division
            complaint = Complaints(
                cat_id=assigned_division,  # ✅ Assign correct division
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
                noc=noc,
                complaindetails=complaindetails,
                compfile=compfile,
                userregid=userreg,
            )
            complaint.save()

            messages.success(request, 'Complaint Lodged Successfully!')
            return redirect("regcomplaint")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
        'compusers': compusers,
    }

    return render(request, 'user/register-complaint-pace.html', context)

#ROC-CSC-CCB REGISTRATION
@login_required(login_url='/')
def CSCCCB(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()
    compusers = UserReg.objects.select_related('admin').all()  # ✅ Fetch all users
    
    print("DEBUG: Users in Dropdown:", compusers)
    
    if request.method == "POST":
        try:
            # ✅ Fetch division from the form
            cat_id = request.POST.get('cat_id')

            # ✅ Get the division category (Promotive Services Division)
            assigned_division = Category.objects.get(id=cat_id)

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
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Generating a unique complaint number
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"CARAGA-FO-ROC-CSCCCB-25-{complaint_number}"

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # ✅ Ensure complaint is assigned to the selected division
            complaint = Complaints(
                cat_id=assigned_division,  # ✅ Assign correct division
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
                noc=noc,
                complaindetails=complaindetails,
                compfile=compfile,
                userregid=userreg,
            )
            complaint.save()

            messages.success(request, 'Complaint Lodged Successfully!')
            return redirect("regcomplaint")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
        'compusers': compusers,
    }

    return render(request, 'user/register-complaint-csc-ccb.html', context)



# #PACDEVEREG REGISTRATION
# @login_required(login_url='/')
# def PACDEVEREG(request):
#     category = Category.objects.all()
#     categorycitymups = Categorycitymup.objects.all()
#     subcategorycitymups = Subcategorycitymup.objects.all()

#     if request.method == "POST":
#         try:
#             # Fetching data from the form
#             cat_id = request.POST.get('cat_id')
#             subcategory_id = request.POST.get('subcategory_id')
#             deadline = request.POST.get('deadline')
#             passed_date = request.POST.get('passed_date')
#             date_received = request.POST.get('date_received')
#             date_endorse = request.POST.get('date_endorse')
#             remind_date = request.POST.get('remind_date')
#             time_received = request.POST.get('time_received')
#             time_acknowledge = request.POST.get('time_acknowledge')
#             time_endorse = request.POST.get('time_endorse')
#             region_name = request.POST.get('region_name', 'Unknown')
#             province_name = request.POST.get('province_name', 'Unknown')
#             city_name = request.POST.get('city_name', 'Unknown')
#             barangay_name = request.POST.get('barangay_name', 'Unknown')
#             selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
#             complaint_email = request.POST.get('complaint_email', '')
#             complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
#             endorseemp  = request.POST.get('endorseemp', 'Unknown')
#             complainant_pace = request.POST.get('complainant_pace', '')
#             complainttype = request.POST.get('complainttype')
#             clientdetails = request.POST.get('clientdetails')
#             noc = request.POST.get('noc')
#             complaindetails = request.POST.get('complaindetails')
#             compfile = request.FILES.get('compfile')

#             # Generating a unique complaint number
#             complaint_number = random.randint(100000000, 999999999)
#             complaint_text = f"CARAGA-FO-ROC-PACD-25-{complaint_number}"

#             # Accessing the UserReg instance associated with the logged-in user
#             userreg = request.user.userreg

#             # Creating the complaint instance
#             complaint = PacdComplaints(
#                 cat_id_id=cat_id,
#                 subcategory_id_id=subcategory_id,
#                 deadline=deadline,
#                 region_name=region_name,
#                 province_name=province_name,
#                 city_name=city_name,
#                 barangay_name=barangay_name,
#                 passed_date=passed_date,
#                 remind_date=remind_date,
#                 date_endorse=date_endorse,
#                 date_received=date_received,
#                 time_received=time_received,
#                 time_endorse=time_endorse,
#                 time_acknowledge=time_acknowledge,
#                 complaint_text=complaint_text,
#                 complainant_fname=complainant_fname,
#                 complainant_pace=complainant_pace,
#                 complaint_email=complaint_email,
#                 selfcomplaint_number=selfcomplaint_number,
#                 complainttype=complainttype,
#                 clientdetails = clientdetails,
#                 noc=noc,
#                 endorseemp=endorseemp,
#                 complaindetails=complaindetails,
#                 compfile=compfile,
#                 userregid=userreg,
#             )
#             complaint.save()

#             messages.success(request, 'Complaint Lodged Successfully!')
#             return redirect("pacdevereg")

#         except Exception as e:
#             messages.error(request, f"An unexpected error occurred: {e}")

#     context = {
#         'category': category,
#         'categorycitymups': categorycitymups,
#         'subcategorycitymups': subcategorycitymups,
#     }

#     return render(request, 'user/register-pacdevereg.html', context)


@login_required(login_url='/')
def COMPLAINTHISTORY(request):
    userreg = request.user.userreg
    complaint_list = Complaints.objects.filter(userregid=userreg).order_by('-complaintdate_at')
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
    return render(request, 'user/complaint-history.html', context)

@login_required(login_url='/')
def USERDASHBOARDHISTORY(request):
    userreg = request.user.userreg
    complaint_list = Complaints.objects.filter(userregid=userreg).order_by('-complaintdate_at')
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
    return render(request, 'user/userdashboard.html', context)

@login_required(login_url='/')
def COMPLAINTHISTORYDETAILS(request,id):
    complaints = Complaints.objects.get(id=id)
    complaintsremarks = ComplaintRemark.objects.filter(comp_id_id=id)
      
    context = {
         'complaints':complaints,
         'complaintsremarks':complaintsremarks,
    }
    return render(request,'user/complaint-details.html',context)

@login_required(login_url='/')
def USERDASHBOARDHISTORYDETAILS(request,id):
    complaints = Complaints.objects.get(id=id)
    complaintsremarks = ComplaintRemark.objects.filter(comp_id_id=id)
      
    context = {
         'complaints':complaints,
         'complaintsremarks':complaintsremarks,
    }
    return render(request,'user/complaint-details.html',context)

def USERLODGEDCOMPLAINTSREMARK(request):
    if request.method == 'POST':
        complaint_id = request.POST.get('comp_id')
        remark_text = request.POST.get('remark')
        status = request.POST.get('status')
        
        # Update the Complaints model
        lodged_complaint = Complaints.objects.get(id=complaint_id)
        lodged_complaint.remark = remark_text
        lodged_complaint.status = status
        lodged_complaint.save()
        
        # Create a new ComplaintRemark entry
        new_remark = ComplaintRemark.objects.create(
            comp_id_id=lodged_complaint,  # Pass the Complaints instance here
            remark=remark_text,
            status=status,
            remarkdate=timezone.now()
        )
        
        messages.success(request, "Status updated successfully")
        return redirect('complainthistory')
    else:
        # Handle the GET request if needed
        complaint_id = request.GET.get('comp_id')
        if complaint_id:
            lodged_complaint = get_object_or_404(Complaints, id=complaint_id)
            remarks = ComplaintRemark.objects.filter(comp_id_id=lodged_complaint)
            context = {'complaint': lodged_complaint, 'remarks': remarks}
        else:
            context = {}
             
    return render(request, 'user/complaint-history.html', context)




