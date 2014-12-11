from django.contrib import admin

from .models import Fascicolo

class FascicoloAdmin(admin.ModelAdmin):
    list_display = ("status", "approval_date", "publication_date","execution_date","initiative")
    #list_filter = ["approvazione", ]
    
    search_fields = ["acts_support__support_type", "acts_support__support_date", ]

admin.site.register(Fascicolo, FascicoloAdmin)