from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.db import models

from open_municipio.acts.admin import ActAdmin, TransitionInline, AttachInline

from .models import Determina, InstitutionCharge, Act
from ..commons.widgets import AdvancedFilteredSelectMultiple


class DeterminaAdminForm(forms.ModelForm): 

    class Meta:
        widgets = {
            'recipient_set': AdvancedFilteredSelectMultiple("Recipients", is_stacked=True, attrs={'size':24})
        }

#class FascicoloAdmin(admin.ModelAdmin):
class DeterminaAdmin(ActAdmin):

    list_display = ("status", "approval_date", "publication_date","execution_date","initiative")
    search_fields = ["acts_support__support_type", "acts_support__support_date", ]

    # NB don't use filter_horizontal, otherwise it would "override" our customization
    # since the form uses FitleredSelectMultiple, it already includes the effect 
    # of flag "filter_horizontal"
    form = DeterminaAdminForm  

    inline_base = [ TransitionInline, AttachInline, ]    

admin.site.register(Determina, DeterminaAdmin)
#admin.site.unregister(Act)
