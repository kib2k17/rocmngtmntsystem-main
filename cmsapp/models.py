from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


#Division
class Category(models.Model):
    catname = models.CharField(max_length=200)
    catdes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.catname
    
#SECTION
class Subcategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcatname
    
    
class CustomUser(AbstractUser):
    USER = [
        (1, 'admin'), #SuperAdmin  
        (2, 'compuser'), #admin
        (3, 'moderator'), #PACD
        (4, 'sememoderator'), #Odsus
    ]

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic', blank=True, null=True)
    
    # ForeignKey for Division and Section
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

    


#City and Municipalality    
class Categorycitymup(models.Model):
    catcitymupname = models.CharField(max_length=200)
    catcitymupdes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.catcitymupname

class Subcategorycitymup(models.Model):
    catmupname_id = models.ForeignKey(Categorycitymup, on_delete=models.CASCADE)
    subcatcitymupname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcatcitymupname

class State(models.Model):
    statename = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.statename

class UserReg(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Division
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)  # Section
    mobilenumber = models.CharField(max_length=11)
    regdate_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.admin:
            return f"{self.admin.first_name} {self.admin.last_name} - {self.mobilenumber}"
        else:
            return f"User not associated - {self.mobilenumber}"

class Complaints(models.Model):
    userregid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True, blank=True)
    
    # # Foreign keys for City and Municipality categories
    # catmupname_id = models.ForeignKey(Categorycitymup, on_delete=models.CASCADE, null=True, blank=True)
    # subcategorycitymup_id = models.ForeignKey(Subcategorycitymup, on_delete=models.CASCADE, null=True, blank=True)

    # Other category-related fields
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    # Dates and times
    deadline = models.DateField(null=True, blank=True)
    passed_date = models.DateField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    date_endorse = models.DateField(null=True, blank=True)
    remind_date = models.DateField(null=True, blank=True)
    time_received = models.TimeField(null=True, blank=True)
    time_acknowledge = models.TimeField(null=True, blank=True)
    time_endorse = models.TimeField(null=True, blank=True)

    #Complete Address Details
    region_name = models.CharField(max_length=250, blank=True, null=True)
    province_name = models.CharField(max_length=250, blank=True, null=True)
    city_name = models.CharField(max_length=250, blank=True, null=True)
    barangay_name = models.CharField(max_length=250, blank=True, null=True)

    # Complaint details
    complaint_number = models.IntegerField(default=0)
    selfcomplaint_number = models.CharField(max_length=50, blank=True, null=True)
    complainant_pace = models.CharField(max_length=250, default='No ticket number provided')
    complaint_email = models.EmailField(max_length=255, blank=True, null=True)
    complaint_text = models.CharField(max_length=255)
    complainttype = models.CharField(max_length=250)
    clientdetails = models.CharField(max_length=250, blank=True, null=True)
    
    cog = models.CharField(max_length=250, blank=True, null=True)


    noc = models.CharField(max_length=250)
    endorseemp = models.CharField(max_length=250, blank=True, null=True)
    complainant_fname = models.CharField(max_length=250, default='Anonymous')
    complaindetails = models.TextField(blank=True)
    compfile = models.ImageField(upload_to='media/doc_file', blank=True, null=True)
    complaintdate_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True)
    status = models.CharField(max_length=250, default='0')
    updated_at = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.complaint_text

    def save(self, *args, **kwargs):
        if not self.complainant_fname:
            self.complainant_fname = 'Anonymous'
        if not self.complainant_pace:
            self.complainant_pace = 'No ticket number provided'
        if not self.selfcomplaint_number:
            self.selfcomplaint_number = "No mobile number provided"
        if not self.complaint_email:
            self.complaint_email = "No email provided"

        super().save(*args, **kwargs)


class ComplaintRemark(models.Model):
    comp_id_id = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    remark = models.TextField(blank=True)
    status = models.CharField(max_length=250,default=0)
    remarkdate = models.DateTimeField(auto_now_add=True)
    
    
    
class PacdComplaints(models.Model):
    userregid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True, blank=True)
    
    # # Foreign keys for City and Municipality categories
    # catmupname_id = models.ForeignKey(Categorycitymup, on_delete=models.CASCADE, null=True, blank=True)
    # subcategorycitymup_id = models.ForeignKey(Subcategorycitymup, on_delete=models.CASCADE, null=True, blank=True)

    # Other category-related fields
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    # Dates and times
    deadline = models.DateField(null=True, blank=True)
    passed_date = models.DateField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    date_endorse = models.DateField(null=True, blank=True)
    remind_date = models.DateField(null=True, blank=True)
    time_received = models.TimeField(null=True, blank=True)
    time_acknowledge = models.TimeField(null=True, blank=True)
    time_endorse = models.TimeField(null=True, blank=True)

    #Complete Address Details
    region_name = models.CharField(max_length=250, blank=True, null=True)
    province_name = models.CharField(max_length=250, blank=True, null=True)
    city_name = models.CharField(max_length=250, blank=True, null=True)
    barangay_name = models.CharField(max_length=250, blank=True, null=True)

    # Complaint details
    complaint_number = models.IntegerField(default=0)
    selfcomplaint_number = models.CharField(max_length=50, blank=True, null=True)
    complainant_pace = models.CharField(max_length=250, default='No ticket number provided')
    complaint_email = models.EmailField(max_length=255, blank=True, null=True)
    complaint_text = models.CharField(max_length=255)
    complainttype = models.CharField(max_length=250)
    clientdetails = models.CharField(max_length=250, blank=True, null=True)

    cog = models.CharField(max_length=250, blank=True, null=True)

    noc = models.CharField(max_length=250)
    endorseemp = models.CharField(max_length=250, blank=True, null=True)
    complainant_fname = models.CharField(max_length=250, default='Anonymous')
    complaindetails = models.TextField(blank=True)
    compfile = models.ImageField(upload_to='media/doc_file', blank=True, null=True)
    complaintdate_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True)
    status = models.CharField(max_length=250, default='Closed')
    updated_at = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.complaint_text

    def save(self, *args, **kwargs):
        if not self.complainant_fname:
            self.complainant_fname = 'Anonymous'
        if not self.complainant_pace:
            self.complainant_pace = 'No ticket number provided'
        if not self.selfcomplaint_number:
            self.selfcomplaint_number = "No mobile number provided"
        if not self.complaint_email:
            self.complaint_email = "No email provided"

        super().save(*args, **kwargs)


class PacdComplaintRemark(models.Model):
    comp_id_id = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    remark = models.TextField(blank=True)
    status = models.CharField(max_length=250, default='Closed')  # Optional initial default
    remarkdate = models.DateTimeField(auto_now_add=True)
    
    
class Odsus(models.Model):
    userregid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True, blank=True)
    complaints = models.ManyToManyField(Complaints, related_name="odsus_entries")
    
    # # Foreign keys for City and Municipality categories
    # catmupname_id = models.ForeignKey(Categorycitymup, on_delete=models.CASCADE, null=True, blank=True)
    # subcategorycitymup_id = models.ForeignKey(Subcategorycitymup, on_delete=models.CASCADE, null=True, blank=True)

    # Other category-related fields
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    # Dates and times
    deadline = models.DateField(null=True, blank=True)
    passed_date = models.DateField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    date_endorse = models.DateField(null=True, blank=True)
    remind_date = models.DateField(null=True, blank=True)
    time_received = models.TimeField(null=True, blank=True)
    time_acknowledge = models.TimeField(null=True, blank=True)
    time_endorse = models.TimeField(null=True, blank=True)

    #Complete Address Details
    region_name = models.CharField(max_length=250, blank=True, null=True)
    province_name = models.CharField(max_length=250, blank=True, null=True)
    city_name = models.CharField(max_length=250, blank=True, null=True)
    barangay_name = models.CharField(max_length=250, blank=True, null=True)

    # Complaint details
    complaint_number = models.IntegerField(default=0)
    selfcomplaint_number = models.CharField(max_length=50, blank=True, null=True)
    complainant_pace = models.CharField(max_length=250, default='No ticket number provided')
    complaint_email = models.EmailField(max_length=255, blank=True, null=True)
    complaint_text = models.CharField(max_length=255)
    complainttype = models.CharField(max_length=250)
    clientdetails = models.CharField(max_length=250, blank=True, null=True)

    cog = models.CharField(max_length=250, blank=True, null=True)

    noc = models.CharField(max_length=250)
    endorseemp = models.CharField(max_length=250, blank=True, null=True)
    complainant_fname = models.CharField(max_length=250, default='Anonymous')
    complaindetails = models.TextField(blank=True)
    compfile = models.ImageField(upload_to='media/doc_file', blank=True, null=True)
    complaintdate_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True)
    status = models.CharField(max_length=250, default='Closed')
    updated_at = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.complaint_text

    def save(self, *args, **kwargs):
        if not self.complainant_fname:
            self.complainant_fname = 'Anonymous'
        if not self.complainant_pace:
            self.complainant_pace = 'No ticket number provided'
        if not self.selfcomplaint_number:
            self.selfcomplaint_number = "No mobile number provided"
        if not self.complaint_email:
            self.complaint_email = "No email provided"

        super().save(*args, **kwargs)


class OdsusRemark(models.Model):
    comp_id_id = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    remark = models.TextField(blank=True)
    status = models.CharField(max_length=250, default='Closed')  # Optional initial default
    remarkdate = models.DateTimeField(auto_now_add=True)


