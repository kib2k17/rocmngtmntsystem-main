from django.contrib import admin
from .models import Category, CustomUser, Subcategory, Subcategorycitymup, State, UserReg, Complaints, ComplaintRemark, Categorycitymup, PacdComplaints, PacdComplaintRemark, Odsus, OdsusRemark, UserActivityLog
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display =['username','email','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(State)
admin.site.register(UserReg)
admin.site.register(Complaints)
admin.site.register(ComplaintRemark)
admin.site.register(Categorycitymup)
admin.site.register(Subcategorycitymup)
admin.site.register(PacdComplaints)
admin.site.register(PacdComplaintRemark)
admin.site.register(Odsus)
admin.site.register(OdsusRemark)

@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')



# #Address
# admin.site.register(Province)
# admin.site.register(City)
# admin.site.register(Barangay)
# admin.site.register(CompleteAddress)