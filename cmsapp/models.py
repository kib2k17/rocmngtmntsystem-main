from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER ={
        (1,'admin'),
        (2,'compuser'),
        
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')

# #BARANGAY

# class Province(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     name = models.CharField(max_length=100)
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')

#     def __str__(self):
#         return f'{self.name}, {self.province.name}'

# class Barangay(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='barangays')

#     def __str__(self):
#         return f'{self.name}, {self.city.name}, {self.city.province.name}'

# class CompleteAddress(models.Model):
#     barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'{self.barangay.name}, {self.barangay.city.name}, {self.barangay.city.province.name}'
    



class Category(models.Model):
    catname = models.CharField(max_length=200)
    catdes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.catname

class Subcategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcatname
    


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
    
    # Foreign keys for City and Municipality categories
    catmupname_id = models.ForeignKey(Categorycitymup, on_delete=models.CASCADE, null=True, blank=True)
    subcategorycitymup_id = models.ForeignKey(Subcategorycitymup, on_delete=models.CASCADE, null=True, blank=True)

    # Other category-related fields
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    # Dates and times
    deadline = models.DateField(null=True, blank=True)
    passed_date = models.DateField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    time_received = models.TimeField(null=True, blank=True)

    # # Location details
    # province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    # city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    # barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE, null=True, blank=True)

    # Complaint details
    complaint_number = models.IntegerField(default=0)
    selfcomplaint_number = models.CharField(max_length=50, blank=True, null=True)
    complainant_pace = models.CharField(max_length=250, default='No ticket number provided')
    complaint_email = models.EmailField(max_length=255, blank=True, null=True)
    complaint_text = models.CharField(max_length=255)
    complainttype = models.CharField(max_length=250)
    noc = models.CharField(max_length=250)
    complainant_fname = models.CharField(max_length=250, default='Anonymous')
    complaindetails = models.TextField(blank=True)
    compfile = models.ImageField(upload_to='media/doc_file')
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


