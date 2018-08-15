from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site


from users.models import KYProfile, CAProfile, College

class KYprofileInline(admin.StackedInline):
    model = KYProfile
    can_delete = False

class CollegeAdmin(admin.ModelAdmin):

    def Registrations(obj):
        number = KYProfile.objects.filter(college=obj).count()
        return number

    list_max_show_all = 500
    list_display = ('collegeName', Registrations)
    ordering = ('collegeName',)
    search_fields = ('collegeName',)

class CAInline(admin.StackedInline):
    model = CAProfile

class KYProfileAdmin(admin.ModelAdmin):

    def name(obj):
        return obj.full_name

    def email(obj):
        return obj.email

    def ca_id(obj):
        try:
            id_ = obj.caprofile.ca_id
        except:
            id_ = 'NA'
        return id_

    def ca(obj):
        try:
            status = obj.caprofile.is_choosen
        except:
            status = 'NA'
        return status

    list_max_show_all = 500
    list_filter = ('has_ca_profile', 'college__regCount', 'college__collegeName')
    list_display = ('ky_id', name, email, 'college', 'mobile_number','is_paid', 'paid_amt', ca_id)
    search_fields = ('ky_id', 'email', 'college__collegeName', 'full_name', 'mobile_number')
    inlines = [
        CAInline,
    ]
class CAProfileAdmin(admin.ModelAdmin):

    def name(obj):
        return obj.kyprofile.full_name

    def email(obj):
        return obj.kyprofile.email

    def college(obj):
        return obj.kyprofile.college

    def mobile_number(obj):
        return obj.kyprofile.mobile_number

    def reg_num(obj):
        return obj.reg_num

    list_filter = ('is_choosen',)
    list_display = ('ca_id', email, name, college, mobile_number, reg_num)
    search_fields = ('ca_id', 'kyprofile__college__collegeName', 'kyprofile__full_name')


# admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.register(KYProfile, KYProfileAdmin)
admin.site.register(CAProfile, CAProfileAdmin)
admin.site.register(College, CollegeAdmin)
