from django.contrib import admin

from .models import *


admin.site.register(Company)

admin.site.register(CompanyInfo)

admin.site.register(CompanyContacts)
admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(WebSite)
admin.site.register(Address)

admin.site.register(CompanyFiles)
admin.site.register(File)
admin.site.register(Image)