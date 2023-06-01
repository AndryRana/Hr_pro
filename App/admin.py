from django.contrib import admin
from .models import Candidate
from django.utils.html import format_html
from .forms import CandidateForm


class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {'smoker': admin.HORIZONTAL}
    form = CandidateForm
    exclude=['status']
    list_filter = ['Situation']
    list_display = ['name','job', 'email', 'phone','created_at', 'status', '_' ]
    search_fields = ['firstname', 'lastname', 'email', 'Situation']
    list_per_page = 10
    
    # Readonly section
    readonly_fields = ['experience','firstname','lastname','job','email','birth','phone','salary',
    'personality','gender','smoker','file','frameworks','languages','databases','libraries',
    'mobile','others','message','image','institution','about_course','course','status_course','started_course', 
    'finished_course','company','position','about_job','started_job', 'finished_job','employed','remote','travel']
    
    
    # FIELDSET
    fieldsets = [
        # HR Operations
        ("HR OPERATIONS", {"fields": ['Situation','company_note']}),
        # PERSONAL
        ("PERSONAL", {"fields": ['experience','gender','job','email','phone','salary','birth','personality','smoker','file', 'image','message']}),
        # SKILLS
        ("SKILLS", {"fields": ['frameworks','languages','databases','libraries','mobile','others']}),
        # EDUCATION
        ("EDUCATION", {"fields": ['status_course','started_course','finished_course','institution','course','about_course']}),
        # Professional
        ("PROFESSIONNAL", {"fields": ['started_job','finished_job','company','position','about_job']}),
        # Note
        ("NOTE", {"fields": ['employed','remote', 'travel']}),
        
        
    ]
    
    # Function to hide F-name and L-name (When clicking over the candidates - Rows)
    def get_fields(self, request, obj = None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('firstname')
            fields.remove('lastname')
        return fields
    
    # Function to change the icons
    def _(self,obj):
        if obj.Situation == 'Approved':
            return True
        elif obj.Situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    
    # Function to color the text field
    def status(self,obj):
        if obj.Situation == 'Approved':
            color = '#28a745'
        elif obj.Situation == 'Pending':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color,obj.Situation))
    status.allow_tags =True
        
        
        
admin.site.register(Candidate, CandidateAdmin)
