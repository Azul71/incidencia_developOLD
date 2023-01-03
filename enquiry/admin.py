from django.contrib import admin
from .models import Enquiry,Follow_ups,Received,Roles,Status,TypeFollowUp,Concello
#,account,Batch
# Register your models here.

	
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','title',]


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','razonsocial','status','asigned',]

admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(Received)
admin.site.register(Follow_ups)
admin.site.register(Status,StatusAdmin)
admin.site.register(TypeFollowUp)
admin.site.register(Concello)
#admin.site.register(Roles)

