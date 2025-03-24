from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from collections import defaultdict

from cmsapp.models import CustomUser,UserReg,Category,Subcategory,Complaints,ComplaintRemark, Categorycitymup, Subcategorycitymup, PacdComplaints, PacdComplaintRemark,Odsus, OdsusRemark
from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from datetime import timedelta
from django.utils.timezone import now, localtime
from datetime import date, timedelta, datetime
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

    # Get user's assigned division and section
    user_division = user_reg.cat
    user_section = user_reg.subcategory

    # ✅ Define complaint categories
    categories = {
        "CARAGA-FO-ROC-DIR-25": "Directory",
        "CARAGA-FO-ROC-INQ-25": "Inquiry",
        "CARAGA-FO-ROC-PACE-25": "Pace",
        "CARAGA-FO-ROC-CSCCCB-25": "CSCCCB",
        "CARAGA-FO-ROC-ARTA-25": "ARTA",
        "CARAGA-FO-ROC-IGRMS-25": "IGRMS",
        "CARAGA-FO-ROC-PACD-25": "PACD",
        "CARAGA-FO-ROC-8888-25": "8888",
    }

    complaint_counts = {
    "CARAGA-FO-ROC-DIR-25": Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-DIR-25").count(),
    "CARAGA-FO-ROC-INQ-25": Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-INQ-25").count(),
    "CARAGA-FO-ROC-PACE-25": Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-PACE-25").count(),
    "CARAGA-FO-ROC-CSCCCB-25": Complaints.objects.filter(complaint_text__startswith="CARAGA-FO-ROC-CSCCCB-25").count(),
    }

    # ✅ Count new complaints with status = '0' (New)
    new_tickets_count = Complaints.objects.filter(status='0').count()

    

    # ✅ Query complaints using Q()
    complaints = Complaints.objects.filter(
        Q(cat_id=user_division, subcategory_id=user_section) |  # User's assigned division & section
        Q(complaint_text__startswith=tuple(categories))  # Show all complaints with specific prefixes
    ).distinct().order_by('-complaintdate_at')

    # ✅ Query for nearing deadline complaints (within the next 3 days)
    today = date.today()
    tickets = Complaints.objects.all()

    nearing_deadline_tickets = []
    for ticket in tickets:
        if isinstance(ticket.remind_date, str):
            # Convert string to date object
            ticket.remind_date = datetime.strptime(ticket.remind_date, '%Y-%m-%d').date()
        nearing_deadline_tickets.append(ticket)

    # ✅ Count complaints based on prefixes
    complaint_counts = {category: complaints.filter(complaint_text__startswith=category).count() for category in categories}

    # ✅ Complaint Status Breakdown
    roc_stats = defaultdict(lambda: {"NEW": 0, "IN_PROCESS": 0, "RESOLVED": 0, "CLOSED": 0})

    for complaint in complaints:
        for code, name in categories.items():
            if complaint.complaint_text.startswith(code):
                status_key = {
                    "0": "NEW",
                    "inprocess": "IN_PROCESS",
                    "resolved": "RESOLVED",
                    "closed": "CLOSED"
                }.get(complaint.status.lower(), None)

                if status_key:
                    roc_stats[name][status_key] += 1


    # ✅ Pagination
    paginator = Paginator(complaints, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # ✅ Overall Complaint Counts
    complaints_count = complaints.count()
    newcom_count = complaints.filter(status='0').count()
    ipcom_count = complaints.filter(status='Inprocess').count()
    resolved_count = complaints.filter(status='Resolved').count()
    closed_count = complaints.filter(status='Closed').count()

    # ✅ Check if the table should be shown
    show_table = any(sum(status_counts.values()) > 0 for status_counts in roc_stats.values())

    # ✅ Pass context to the template
    context = {
        'page_obj': page_obj,
        'complaints_count': complaints_count,
        'newcom_count': newcom_count,
        'ipcom_count': ipcom_count,
        'resolved_count': resolved_count,
        'closed_count': closed_count,
        'nearing_deadline_tickets': nearing_deadline_tickets,
        'now': today,
        'roc_stats': dict(roc_stats),
        'show_table': show_table,
        'new_tickets_count': new_tickets_count,
        'dir_complaint_count': complaint_counts.get("CARAGA-FO-ROC-DIR-25", 0),
        'dir_complaint_count2': complaint_counts.get("CARAGA-FO-ROC-INQ-25", 0),
        'dir_complaint_count3': complaint_counts.get("CARAGA-FO-ROC-PACE-25", 0),
        'dir_complaint_count4': complaint_counts.get("CARAGA-FO-ROC-CSCCCB-25", 0),
        'dir_complaint_count5': 0,  # If you want to add "Total 8888", update this dynamically
        **complaint_counts  # Dynamically pass complaint counts
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


@login_required
def NEWCOMPLAINTS(request):
    user_admin = request.user  # Get logged-in user

    # Get the user's registration details safely
    user_reg = UserReg.objects.filter(admin=user_admin).first()
    if not user_reg:
        return HttpResponse("User registration details not found.", status=404)

    # Access division & section from user model
    user_division_id = user_reg.cat_id  # Ensure it's an ID
    user_section_id = user_reg.subcategory_id  # Ensure it's an ID

    # Filter complaints based on user's division (cat) & section (subcategory)
    odsusnewcomplaints = Complaints.objects.filter(
        cat_id=user_division_id,
        subcategory_id=user_section_id,
        status="0"  # Ensure the correct field name and value
    ).order_by('-complaintdate_at')

    context = {'odsusnewcomplaints': odsusnewcomplaints}
    return render(request, 'odsus/new-complaints.html', context)




def INPROCESSCOMPLAINTS(request):    
    user_admin = request.user  # Get logged-in user

    # Get the user's registration details safely
    user_reg = UserReg.objects.filter(admin=user_admin).first()
    if not user_reg:
        return HttpResponse("User registration details not found.", status=404)

    # Access division & section from user model
    user_division_id = user_reg.cat_id  # Ensure it's an ID
    user_section_id = user_reg.subcategory_id  # Ensure it's an ID

    # Filter complaints based on user's division (cat) & section (subcategory)
    odsusinprocesscomplaints = Complaints.objects.filter(
        cat_id=user_division_id,
        subcategory_id=user_section_id,
        status="Inprocess"  # Ensure the correct field name and value
    ).order_by('-complaintdate_at')

    context = {'odsusinprocesscomplaints': odsusinprocesscomplaints}
    return render(request, 'odsus/inprocess_complaints.html', context)

def RESOLVEDCOMPLAINTS(request):    
    user_admin = request.user  # Get logged-in user

    # Get the user's registration details safely
    user_reg = UserReg.objects.filter(admin=user_admin).first()
    if not user_reg:
        return HttpResponse("User registration details not found.", status=404)

    # Access division & section from user model
    user_division_id = user_reg.cat_id  # Ensure it's an ID
    user_section_id = user_reg.subcategory_id  # Ensure it's an ID

    # Filter complaints based on user's division (cat) & section (subcategory)
    odsusresolvedcomplaints = Complaints.objects.filter(
        cat_id=user_division_id,
        subcategory_id=user_section_id,
        status="Resolved"  # Ensure the correct field name and value
    ).order_by('-complaintdate_at')

    context = {'odsusresolvedcomplaints': odsusresolvedcomplaints}
    return render(request, 'odsus/resolved_complaints.html', context)

def CLOSEDCOMPLAINTS(request):    
    user_admin = request.user  # Get logged-in user

    # Get the user's registration details safely
    user_reg = UserReg.objects.filter(admin=user_admin).first()
    if not user_reg:
        return HttpResponse("User registration details not found.", status=404)

    # Access division & section from user model
    user_division_id = user_reg.cat_id  # Ensure it's an ID
    user_section_id = user_reg.subcategory_id  # Ensure it's an ID

    # Filter complaints based on user's division (cat) & section (subcategory)
    odsusclosedcomplaints = Complaints.objects.filter(
        cat_id=user_division_id,
        subcategory_id=user_section_id,
        status="Closed"  # Ensure the correct field name and value
    ).order_by('-complaintdate_at')

    context = {'odsusclosedcomplaints': odsusclosedcomplaints}
    return render(request, 'odsus/closed_complaints.html', context)

@login_required(login_url='/')
def LODGEDCOMPLAINTS(request):
    user = request.user

    # Get the user's registration details
    user_reg = UserReg.objects.filter(admin=user).first()
    if not user_reg:
        return HttpResponse("User registration details not found.", status=404)

    # Get user division and section
    user_division_id = user_reg.cat_id
    user_section_id = user_reg.subcategory_id

    # ✅ Direktang filtering (gaya sa NEWCOMPLAINTS)
    complaints = Complaints.objects.filter(
        cat_id=user_division_id,
        subcategory_id=user_section_id
    ).order_by('-complaintdate_at')

    # ✅ Pagination
    paginator = Paginator(complaints, 10)
    page_number = request.GET.get('page')
    
    try:
        complaints_page = paginator.page(page_number)
    except PageNotAnInteger:
        complaints_page = paginator.page(1)
    except EmptyPage:
        complaints_page = paginator.page(paginator.num_pages)

    context = {
        'complaints': complaints_page,
    }
    return render(request, 'odsus/lodged-complaints.html', context)


@login_required(login_url='/')
def COMPLAINTSREPORT(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    odsuslodgedcomplaints = []

    if start_date and end_date:
        try:
            # ✅ Convert to datetime para sakto sa DateTimeField
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)
        except ValueError:
            return render(request, 'odsus/complaint-between-date-report.html', {
                'odsuslodgedcomplaints': odsuslodgedcomplaints,
                'error_message': 'Invalid date format'
            })

        user = request.user
        user_reg = UserReg.objects.filter(admin=user).first()

        if user_reg:
            user_division_id = user_reg.cat_id
            user_section_id = user_reg.subcategory_id

            # ✅ Debugging (para ma-check natin kung may value)
            print(f"User Division ID: {user_division_id}")
            print(f"User Section ID: {user_section_id}")

            # ✅ Limit data based on user division and section (kahit admin pa)
            if user_division_id and user_section_id:
                odsuslodgedcomplaints = Complaints.objects.filter(
                    cat_id=user_division_id,
                    subcategory_id=user_section_id,
                    complaintdate_at__range=(start_date, end_date)
                ).order_by('-complaintdate_at')
                print(f"Filtered complaints count: {odsuslodgedcomplaints.count()}")

    context = {
        'odsuslodgedcomplaints': odsuslodgedcomplaints,
        'start_date': start_date.date() if start_date else '',
        'end_date': end_date.date() if end_date else ''
    }

    return render(request, 'odsus/complaint-between-date-report.html', context)