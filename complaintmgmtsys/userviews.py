from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

from cmsapp.models import CustomUser,UserReg,Category,Subcategory,Complaints,ComplaintRemark, Categorycitymup, Subcategorycitymup
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import random



@login_required(login_url='/')

def USERHOME(request):
    complaints = Complaints.objects.all().order_by('remind_date')
    user_admin = request.user
    user_reg = UserReg.objects.get(admin=user_admin)
    complaints_count = Complaints.objects.filter(userregid=user_reg).count()
    newcom_count = Complaints.objects.filter(status='0',userregid=user_reg).count()
    ipcom_count = Complaints.objects.filter(status='Inprocess',userregid=user_reg).count()
    closed_count = Complaints.objects.filter(status='Closed',userregid=user_reg).count()
    context = {
    'complaints':complaints,
    'complaints_count':complaints_count,
    'newcom_count':newcom_count,
    'ipcom_count':ipcom_count,
    'closed_count':closed_count,        
    }
    return render(request,'user/userdashboard.html',context)




def USERSIGNUP(request):
   
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
            return redirect('usersignup')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist')
            return redirect('usersignup')
        else:
            user = CustomUser(
               first_name=first_name,
               last_name=last_name,
               username=username,
               email=email,
               user_type=2,
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
    
    

    return render(request,'user/user_reg.html')



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




#ROC DIR REGISTRATION
@login_required(login_url='/')
def REGCOMPLAINT(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()

    if request.method == "POST":
        try:
            # Fetching the selected category and subcategory
            cat_id = request.POST.get('cat_id')
            subcategory_id_value = request.POST.get('subcategory_id')

            # Citymupbarangays
            categorycitymups_id = request.POST.get('catmupname_id')
            subcategorycitymups_id = request.POST.get('subcategorycitymup_id')

            # Fetching time and date fields
            deadline = request.POST.get('deadline')
            passed_date = request.POST.get('passed_date')
            date_received = request.POST.get('date_received')
            date_endorse = request.POST.get('date_endorse')
            remind_date = request.POST.get('remind_date')
            time_received = request.POST.get('time_received')
            time_acknowledge = request.POST.get('time_acknowledge')
            time_endorse = request.POST.get('time_endorse')

            # Fetching address-related fields
            # province_id = request.POST['province']
            # city_id = request.POST['city']
            # barangay_id = request.POST['barangay']

            # Generating a random complaint number and getting other data
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"ROC-DIR-24-{complaint_number}"
            selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
            complaint_email = request.POST.get('complaint_email', '')
            complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Fetching the selected Province and City
            try:
                categorycitymups_instance = Categorycitymup.objects.get(id=categorycitymups_id)
            except Categorycitymup.DoesNotExist:
                messages.error(request, "The selected Category City Municipality does not exist.")
                return redirect('regcomplaint')

            try:
                subcategorycitymups_instance = Subcategorycitymup.objects.get(id=subcategorycitymups_id)
            except Subcategorycitymup.DoesNotExist:
                messages.error(request, "The selected Subcategory City Municipality does not exist.")
                return redirect('regcomplaint')

            # Fetching the selected Category and Subcategory
            try:
                cid = Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                messages.error(request, "The selected category does not exist.")
                return redirect('regcomplaint')

            try:
                subcategory_id = Subcategory.objects.get(id=subcategory_id_value)
            except Subcategory.DoesNotExist:
                messages.error(request, "The selected subcategory does not exist.")
                return redirect('regcomplaint')

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Complaints(
                catmupname_id=categorycitymups_instance,  # Passing the instance, not the ID
                subcategorycitymup_id=subcategorycitymups_instance,  # Same here
                cat_id=cid,
                subcategory_id=subcategory_id,
                deadline=deadline,
                passed_date=passed_date,
                remind_date = remind_date,
                date_endorse = date_endorse,
                date_received=date_received,
                time_received=time_received,
                time_endorse = time_endorse,
                time_acknowledge = time_acknowledge,
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

            messages.success(request, 'Complaint Lodged Successfully!!!')
            return redirect("regcomplaint")
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
    
    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
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
            # Fetching the selected category and subcategory
            cat_id = request.POST.get('cat_id')
            subcategory_id_value = request.POST.get('subcategory_id')

            # Citymupbarangays
            categorycitymups_id = request.POST.get('catmupname_id')
            subcategorycitymups_id = request.POST.get('subcategorycitymup_id')

            # Fetching time and date fields
            deadline = request.POST.get('deadline')
            passed_date = request.POST.get('passed_date')
            date_received = request.POST.get('date_received')
            date_endorse = request.POST.get('date_endorse')
            remind_date = request.POST.get('remind_date')
            time_received = request.POST.get('time_received')
            time_acknowledge = request.POST.get('time_acknowledge')
            time_endorse = request.POST.get('time_endorse')

            # Fetching address-related fields
            # province_id = request.POST['province']
            # city_id = request.POST['city']
            # barangay_id = request.POST['barangay']

            # Generating a random complaint number and getting other data
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"ROC-PACD-24-{complaint_number}"
            selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
            complaint_email = request.POST.get('complaint_email', '')
            complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Fetching the selected Province and City
            try:
                categorycitymups_instance = Categorycitymup.objects.get(id=categorycitymups_id)
            except Categorycitymup.DoesNotExist:
                messages.error(request, "The selected Category City Municipality does not exist.")
                return redirect('pacdcomplaint')

            try:
                subcategorycitymups_instance = Subcategorycitymup.objects.get(id=subcategorycitymups_id)
            except Subcategorycitymup.DoesNotExist:
                messages.error(request, "The selected Subcategory City Municipality does not exist.")
                return redirect('pacdcomplaint')

            # Fetching the selected Category and Subcategory
            try:
                cid = Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                messages.error(request, "The selected category does not exist.")
                return redirect('pacdcomplaint')

            try:
                subcategory_id = Subcategory.objects.get(id=subcategory_id_value)
            except Subcategory.DoesNotExist:
                messages.error(request, "The selected subcategory does not exist.")
                return redirect('pacdcomplaint')

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Complaints(
                catmupname_id=categorycitymups_instance,  # Passing the instance, not the ID
                subcategorycitymup_id=subcategorycitymups_instance,  # Same here
                cat_id=cid,
                subcategory_id=subcategory_id,
                deadline=deadline,
                passed_date=passed_date,
                remind_date = remind_date,
                date_endorse = date_endorse,
                date_received=date_received,
                time_received=time_received,
                time_endorse = time_endorse,
                time_acknowledge = time_acknowledge,
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

            messages.success(request, 'Complaint Lodged Successfully!!!')
            return redirect("pacdcomplaint")
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
    
    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
    }


    return render(request, 'user/register-complaint-pacd.html', context)


@login_required(login_url='/')
def NON8888REGCOMPLAINT(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()

    if request.method == "POST":
        try:
            # Fetching the selected category and subcategory
            cat_id = request.POST.get('cat_id')
            subcategory_id_value = request.POST.get('subcategory_id')

            # Citymupbarangays
            categorycitymups_id = request.POST.get('catmupname_id')
            subcategorycitymups_id = request.POST.get('subcategorycitymup_id')

            # Fetching time and date fields
            deadline = request.POST.get('deadline')
            passed_date = request.POST.get('passed_date')
            date_received = request.POST.get('date_received')
            date_endorse = request.POST.get('date_endorse')
            remind_date = request.POST.get('remind_date')
            time_received = request.POST.get('time_received')
            time_acknowledge = request.POST.get('time_acknowledge')
            time_endorse = request.POST.get('time_endorse')

            # Fetching address-related fields
            # province_id = request.POST['province']
            # city_id = request.POST['city']
            # barangay_id = request.POST['barangay']

            # Generating a random complaint number and getting other data
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"ROC-INQ-24-{complaint_number}"
            selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
            complaint_email = request.POST.get('complaint_email', '')
            complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Fetching the selected Province and City
            try:
                categorycitymups_instance = Categorycitymup.objects.get(id=categorycitymups_id)
            except Categorycitymup.DoesNotExist:
                messages.error(request, "The selected Category City Municipality does not exist.")
                return redirect('non8888regcomplaint')

            try:
                subcategorycitymups_instance = Subcategorycitymup.objects.get(id=subcategorycitymups_id)
            except Subcategorycitymup.DoesNotExist:
                messages.error(request, "The selected Subcategory City Municipality does not exist.")
                return redirect('non8888regcomplaint')

            # Fetching the selected Category and Subcategory
            try:
                cid = Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                messages.error(request, "The selected category does not exist.")
                return redirect('non8888regcomplaint')

            try:
                subcategory_id = Subcategory.objects.get(id=subcategory_id_value)
            except Subcategory.DoesNotExist:
                messages.error(request, "The selected subcategory does not exist.")
                return redirect('non8888regcomplaint')

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Complaints(
                catmupname_id=categorycitymups_instance,  # Passing the instance, not the ID
                subcategorycitymup_id=subcategorycitymups_instance,  # Same here
                cat_id=cid,
                subcategory_id=subcategory_id,
                deadline=deadline,
                passed_date=passed_date,
                remind_date = remind_date,
                date_endorse = date_endorse,
                date_received=date_received,
                time_received=time_received,
                time_endorse = time_endorse,
                time_acknowledge = time_acknowledge,
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

            messages.success(request, 'Complaint Lodged Successfully!!!')
            return redirect("non8888regcomplaint")
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
    
    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
    }


    return render(request, 'user/register-complaint-non-8888.html', context)

#ROC-PACE REGISTRATION
@login_required(login_url='/')
def PACEREGCOMPLAINT(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()

    if request.method == "POST":
        try:
            # Fetching the selected category and subcategory
            cat_id = request.POST.get('cat_id')
            subcategory_id_value = request.POST.get('subcategory_id')

            # Citymupbarangays
            categorycitymups_id = request.POST.get('catmupname_id')
            subcategorycitymups_id = request.POST.get('subcategorycitymup_id')

            # Fetching time and date fields
            deadline = request.POST.get('deadline')
            passed_date = request.POST.get('passed_date')
            date_received = request.POST.get('date_received')
            date_endorse = request.POST.get('date_endorse')
            remind_date = request.POST.get('remind_date')
            time_received = request.POST.get('time_received')
            time_acknowledge = request.POST.get('time_acknowledge')
            time_endorse = request.POST.get('time_endorse')

            # Fetching address-related fields
            # province_id = request.POST['province']
            # city_id = request.POST['city']
            # barangay_id = request.POST['barangay']

            # Generating a random complaint number and getting other data
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"ROC-PACE-24-{complaint_number}"
            selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
            complaint_email = request.POST.get('complaint_email', '')
            complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Fetching the selected Province and City
            try:
                categorycitymups_instance = Categorycitymup.objects.get(id=categorycitymups_id)
            except Categorycitymup.DoesNotExist:
                messages.error(request, "The selected Category City Municipality does not exist.")
                return redirect('paceregcomplaint')

            try:
                subcategorycitymups_instance = Subcategorycitymup.objects.get(id=subcategorycitymups_id)
            except Subcategorycitymup.DoesNotExist:
                messages.error(request, "The selected Subcategory City Municipality does not exist.")
                return redirect('paceregcomplaint')

            # Fetching the selected Category and Subcategory
            try:
                cid = Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                messages.error(request, "The selected category does not exist.")
                return redirect('paceregcomplaint')

            try:
                subcategory_id = Subcategory.objects.get(id=subcategory_id_value)
            except Subcategory.DoesNotExist:
                messages.error(request, "The selected subcategory does not exist.")
                return redirect('paceregcomplaint')

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Complaints(
                catmupname_id=categorycitymups_instance,  # Passing the instance, not the ID
                subcategorycitymup_id=subcategorycitymups_instance,  # Same here
                cat_id=cid,
                subcategory_id=subcategory_id,
                deadline=deadline,
                passed_date=passed_date,
                remind_date = remind_date,
                date_endorse = date_endorse,
                date_received=date_received,
                time_received=time_received,
                time_endorse = time_endorse,
                time_acknowledge = time_acknowledge,
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

            messages.success(request, 'Complaint Lodged Successfully!!!')
            return redirect("non8888regcomplaint")
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
    
    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
    }


    return render(request, 'user/register-complaint-pace.html', context)

#ROC-CSC-CCB REGISTRATION
@login_required(login_url='/')
def CSCCCB(request):
    category = Category.objects.all()
    categorycitymups = Categorycitymup.objects.all()
    subcategorycitymups = Subcategorycitymup.objects.all()

    if request.method == "POST":
        try:
            # Fetching the selected category and subcategory
            cat_id = request.POST.get('cat_id')
            subcategory_id_value = request.POST.get('subcategory_id')

            # Citymupbarangays
            categorycitymups_id = request.POST.get('catmupname_id')
            subcategorycitymups_id = request.POST.get('subcategorycitymup_id')

            # Fetching time and date fields
            deadline = request.POST.get('deadline')
            passed_date = request.POST.get('passed_date')
            date_received = request.POST.get('date_received')
            date_endorse = request.POST.get('date_endorse')
            remind_date = request.POST.get('remind_date')
            time_received = request.POST.get('time_received')
            time_acknowledge = request.POST.get('time_acknowledge')
            time_endorse = request.POST.get('time_endorse')

            # Fetching address-related fields
            # province_id = request.POST['province']
            # city_id = request.POST['city']
            # barangay_id = request.POST['barangay']

            # Generating a random complaint number and getting other data
            complaint_number = random.randint(100000000, 999999999)
            complaint_text = f"ROC-CSC-CCB-24-{complaint_number}"
            selfcomplaint_number = request.POST.get('selfcomplaint_number', 'No mobile number provided')
            complaint_email = request.POST.get('complaint_email', '')
            complainant_fname = request.POST.get('complainant_fname', 'Anonymous')
            complainant_pace = request.POST.get('complainant_pace', '')
            complainttype = request.POST.get('complainttype')
            noc = request.POST.get('noc')
            complaindetails = request.POST.get('complaindetails')
            compfile = request.FILES.get('compfile')

            # Fetching the selected Province and City
            try:
                categorycitymups_instance = Categorycitymup.objects.get(id=categorycitymups_id)
            except Categorycitymup.DoesNotExist:
                messages.error(request, "The selected Category City Municipality does not exist.")
                return redirect('cscccbcomplaint')

            try:
                subcategorycitymups_instance = Subcategorycitymup.objects.get(id=subcategorycitymups_id)
            except Subcategorycitymup.DoesNotExist:
                messages.error(request, "The selected Subcategory City Municipality does not exist.")
                return redirect('cscccbcomplaint')

            # Fetching the selected Category and Subcategory
            try:
                cid = Category.objects.get(id=cat_id)
            except Category.DoesNotExist:
                messages.error(request, "The selected category does not exist.")
                return redirect('cscccbcomplaint')

            try:
                subcategory_id = Subcategory.objects.get(id=subcategory_id_value)
            except Subcategory.DoesNotExist:
                messages.error(request, "The selected subcategory does not exist.")
                return redirect('cscccbcomplaint')

            # Accessing the UserReg instance associated with the logged-in user
            userreg = request.user.userreg

            # Creating the complaint instance
            complaint = Complaints(
                catmupname_id=categorycitymups_instance,  # Passing the instance, not the ID
                subcategorycitymup_id=subcategorycitymups_instance,  # Same here
                cat_id=cid,
                subcategory_id=subcategory_id,
                deadline=deadline,
                passed_date=passed_date,
                remind_date = remind_date,
                date_endorse = date_endorse,
                date_received=date_received,
                time_received=time_received,
                time_endorse = time_endorse,
                time_acknowledge = time_acknowledge,
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

            messages.success(request, 'Complaint Lodged Successfully!!!')
            return redirect("cscccbcomplaint")
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
    
    context = {
        'category': category,
        'categorycitymups': categorycitymups,
        'subcategorycitymups': subcategorycitymups,
    }


    return render(request, 'user/register-complaint-csc-ccb.html', context)
 


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

