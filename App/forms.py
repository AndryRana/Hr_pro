from django import forms
from .models import Candidate, SMOKER, Email
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date # Used in Birth date
import datetime # Used to prevent future date

# Every letters to Lowercase
class Lowercase(forms.CharField):
    def to_python(self,value):
        return value.lower()

# Every letters to Uppercase
class Uppercase(forms.CharField):
    def to_python(self,value):
        return value.upper()

class CandidateForm(forms.ModelForm):
    
    #First name
    firstname = forms.CharField(
        label='First name', 
        min_length=3, max_length=50, 
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only letters is allowed!")], 
        error_messages={'required':'First name cannot be empty.'},
        widget=forms.TextInput(
            attrs={
                'placeholder':'First name',
                'style':'font-size: 13px; text-transform: capitalize'
        })
    )

    # Last name
    lastname = forms.CharField(
        label='Last name', 
        min_length=3, max_length=50, 
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message="Only letters is allowed!")], 
        widget=forms.TextInput(attrs={
            'placeholder':'Last name',
            'style':'font-size: 13px; text-transform: capitalize'
        })
    )
    
    # Job code  (Uppercase Function)
    job = Uppercase(
        label='Job code', 
        min_length=5, max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Example: FR-22',
                'style':'font-size: 13px; text-transform: uppercase',
                'data-mask':'AA-00'
        })
    )
    
    # Email code  (Uppercase Function)
    email = Lowercase(
        label='Email address', 
        min_length=8, max_length=50, 
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+(\.[a-zA-Z]{2,4})+$', 
        message="Put a valid email address!")],
        error_messages={'required':'Email field cannot be empty.'}, 
        widget=forms.TextInput(attrs={
            'placeholder':'Email',
            'style':'font-size: 13px; text-transform: lowercase',
            # 'autocomplete':'off'
        }),
        
    )
    
    # Method 1
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    
    # Method 2
    # age = forms.CharField(
    #     label='Your age', min_length=2, max_length=2, 
    #     validators= [RegexValidator(r'^[0-9]*$', 
    #     message="Only numbers is allowed!")], 
    #     error_messages={'required':'Age field cannot be empty.'},
    #     widget=forms.TextInput(attrs={
    #         'placeholder':'Age',
    #         'style':'font-size: 13px;',
    #         # 'autocomplete':'off'
    #     }),
        
    # )
    
    #Experience
    experience = forms.BooleanField(label="I have experience", required = False)
    
    #Message
    message =  forms.CharField(
        label='About you', min_length=50, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Talk a little about you',
                'rows':7,
                'style':'font-size: 13px;'
            }
        ),
    )
    
    # File (Upload Rsume)
    file = forms.FileField(
        label='Resume',
        widget=forms.ClearableFileInput(
            attrs={
                'style':'font-size: 13px;',
                # 'accept':'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            }
        )
    )
    
    # Photo (Upload photo)
    image = forms.FileField(
        label='Photo',
        widget=forms.ClearableFileInput(
            attrs={
                'style':'font-size: 13px;',
                'accept':'image/png, image/jpeg'
            }
        )
    )
    
    # Institution
    institution = forms.CharField(
        label='Institution',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'style':'font-size: 13px;',
            'placeholder':'Institution name'
        })
    )
    
    
    # College course
    course = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'style':'font-size: 13px;',
            'placeholder':'Your college course'
        })
    )
    
    # About college course
    about_course =  forms.CharField(
        label='About your college course', min_length=50, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Tell us a little about your college course',
                'rows':7,
                'style':'font-size: 13px;'
            }
        ),
    )
   
    # About the job 
    about_job =  forms.CharField(
        label='About your last job', min_length=50, max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Tell us little about what you did at the company...',
                'rows':7,
                'style':'font-size: 13px;'
            }
        ),
    )
   
    # Company (Last Company)
    company = forms.CharField(
        label = 'Last Company',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'style':'font-size: 13px;',
            'placeholder':'Company name'
        })
    )
    
    # Position (Occupation)
    position = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'style':'font-size: 13px;',
            'placeholder':'Your occupation'
        })
    )
    
    employed = forms.BooleanField( label="I'm employed", required=False)
    remote = forms.BooleanField( label='I agree to work remotely', required=False)
    travel = forms.BooleanField( label="I'm available for travel", required=False)
    
    # Method 1 (Gender)
    #GENDER = [('M','Male'), ('F', 'Female')]
    #gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))
    
    class Meta:
        model = Candidate
        #fields = "__all__"
        exclude =['created_at','Situation'] 
        #fields = ['firstname', 'lastname', 'email', 'message','age' ] 
        
        #Label_control
        labels = {
           'started_course': 'Started',
           'finished_course': 'Finished',
           'started_job': 'Started',
           'finished_job': 'Finished',
        }
        
        SALARY = (
            ('', 'Salary Expectation (month)'),
            ('Between ($3000 and $4000)', 'Between ($3000 and $4000)'),
            ('Between ($4000 and $5000)', 'Between ($4000 and $5000)'),
            ('Between ($5000 and $7000)', 'Between ($5000 and $7000)'),
            ('Between ($7000 and $10000)', 'Between ($7000 and $10000)'),
        )
        
        # Methode 2 (Gender)
        GENDER = [('M','Male'), ('F', 'Female')]
        
        
        # Outside Widgets
        widgets = {
            #Birthday
            'birth':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor:pointer',
                    'type':'date',
                    'onkeydown':'event.preventDefault();',# Block typing inside the input
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                }
            ),
            
             # Started course
            'started_course':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor:pointer',
                    'type':'date',
                    'onkeydown':'event.preventDefault();',
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                }
            ),
            
            # Finished course
            'finished_course':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor:pointer',
                    'type':'date',
                    'onkeydown':'event.preventDefault();',
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                }
            ),
            
            # Started job
            'started_job':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor:pointer',
                    'type':'date',
                    'onkeydown':'event.preventDefault();',
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                }
            ),
            
            # Finished job
            'finished_job':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor:pointer',
                    'type':'date',
                    'onkeydown':'event.preventDefault();',
                    'min':'1950-01-01',
                    'max':'2030-01-01'
                }
            ),
    
            
            #Phone
            'phone': forms.TextInput(
                attrs={
                    'style':'font-size:13px;',
                    'placeholder':'Phone', 
                    'data-mask':'+0 (00) 000-0000'
                }
            ),
            #Salary
            'salary': forms.Select(
                choices=SALARY,
                attrs={
                    'class':'form-control',#bootstrap inside the forms.py
                    'style':'font-size: 13px;'
                }
            ),
            #Gender
            'gender':forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check' }),
            'smoker':forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check' }),
            'personality':forms.Select(attrs={'style':'font-size: 13px;'}),
            'status_course':forms.Select(attrs={'style':'font-size: 13px;'}),
            
        }
        
    # ------------------------------------------ SUPER FUNCTION--------------------------------|
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        
        # Disable all Inputs (By: ID/PK)
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #     self.fields['firstname'].disabled= True
        
        # ============ CONTROL PANEL (individual <Input>)============|
        # 1) Input required
        #self.fields['message'].required = True
        
        # 2) Input disabled
        #self.fields['experience'].disabled=False
        
        # 3) Input Readonly
        #self.fields['email'].widget.attrs.update({'readonly': 'readonly'})
         
        # 4) SELECT OPTION
        # self.fields["personality"].choices = [("", "Select a personality"),] + list(self.fields["personality"].choices)[1:]
        
        # 5) WIDGET (inside/outside)
        # self.fields['phone'].widget.attrs.update({'style': 'font-size: 15px', 'placeholder':'No phone'})
        
        # 6) ERROR MESSAGES
        #self.fields['firstname'].error_messages.update({'required':'Les champs sont obligatoire'})
        
        # ============ ADVANCED CONTROL PANEL (multiple input )READONLY / DISABLED BY 'LOOP FOR' IN [ARRAY]============|
        # 1) readonly
        #readonly = ['firstname', 'lastname','job','email', 'age', 'phone']
        #for field in readonly:
         #   self.fields[field].widget.attrs['readonly'] = 'true'
            
        # 2) Disabled
        #disabled= ['personality', 'salary','gender','smoker', 'experience']
        #for field in disabled:
        #    self.fields[field].widget.attrs['disabled'] = 'true'
        
        # 3) ERROR MESSAGES
        # error_messages = ['firstname', 'lastname', 'job','email','age','phone', 'personality','salary', 'gender', 'smoker']
        # for field in error_messages:
        #     self.fields[field].error_messages.update({'required': 'Les champs sont obligatoires!'})
        
        # 4) FONT SIZE
        # font_size= ['firstname', 'lastname', 'job','email','age','phone', 'personality','salary','file']
        # for field in font_size:
        #    self.fields[field].widget.attrs.update({"style":"font-size:16px" })
        
        # 5) AUTO COMPLETE = OFF (Input History DON'T USE READONLY in Admin.py to avoid error)
        # auto_complete= ['firstname', 'lastname','email','phone']
        # for field in auto_complete:
        #    self.fields[field].widget.attrs.update({"autocomplete":"off" })
        
        # 6)  DISABLE ALL INPUT (By: ID/PK)
        # instance = getattr(self, 'instance', None)
        # array =  ['experience','firstname','lastname','job','email','birth','phone','salary',
        # 'personality','gender','smoker','file','frameworks','languages','databases','libraries',
        # 'mobile','others','message','image','institution','about_course','course','status_course','started_course', 
        # 'finished_course','company','position','about_job','started_job', 'finished_job','employed','remote','travel']
        
        # for field in array:
        #     if instance and instance.pk:
        #         self.fields[field].disabled = True
        #         self.fields['file'].widget.attrs.update({'style':'display:none'})
        #         self.fields['image'].widget.attrs.update({'style':'display:none'})
            
    # ------------------------------------------END // SUPER FUNCTION-----------------------------------|
        
    #============================================= FUNCTION (METHOD CLEAN) ============================================= | 
    # 1) FUNCTION TO PREVENT DUPLICATED ENTRIES
    # METHOD 1 (loop for)
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError('Denied !  {}  is already registered.'.format(email))
    #     return email
    
    # Method 2 (if statement w/ filter)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email=email).exists():
            raise forms.ValidationError('Denied !  {}  is already registered.'.format(email))
        return email
        
    # 2) JOB CODE (Job code validation)
    def clean_job(self):
        job = self.cleaned_data.get('job')
        if job == 'FR-22' or job == 'BA-10' or job == 'FU-15':
            return job
        else:
            raise forms.ValidationError('Denied! This code is invalid!')
        
    # 3)AGE (Range: 18 - 65)
    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     if age < '18' or age > '65':
    #         raise forms.ValidationError('Denied ! Age must be between 18 and 65.')
    #     return age
    
    # 4) PHONE (Prevent incomplete values)
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if  len(phone) != 16:
            raise forms.ValidationError('Denied ! Phone field is incomplete.')
        return phone
    
    # 5) RESTRICTION (file extensions - method 2 via function)
    # def clean_file(self):
    #     file = self.cleaned_data.get('file')
    #     content_type = file.content_type
    #     if content_type == 'application/pdf' or content_type =='application/msword' or content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    #         return file
    #     else:
    #         raise forms.ValidationError('Only: PDF - DOC - DOCX')
            
    # Method 3 
    def clean_file(self):
        # Get data
        file = self.cleaned_data.get('file', False)
        # Variables
        EXT = [ 'pdf', 'doc','docx']
        ext = str(file).split('.')[-1]
        type = ext.lower()
        # Statements
        # a) Accept only pdf - doc - docx
        if type not in EXT:
            raise forms.ValidationError('Only: PDF - DOC - DOCX')
        # b) Prevent upload more than 2MB
        if file.size > 2 * 1048476:
            raise forms.ValidationError('Denied ! Maximum allowed is 2 MB.')
        return file
    
    # 6) IMAGE (MAximum upload size = 2MB)
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if  image.size > 2 * 1048476:
            raise forms.ValidationError('Denied ! Maximum allowed is 2 MB.')
        return image
    
    # 7) BIRTHDAY (Range:18 and 65)
    def clean_birth(self):
        birth = self.cleaned_data.get('birth')
        # Variables
        b = birth
        now = date.today()
        # the expression (now.month, now.day) < (b.month, b.day) compares the tuples (now.month, now.day) and (b.month, b.day). 
        # This comparison returns a Boolean value (True or False), 
        # which is then converted to an integer (1 for True and 0 for False) and subtracted from the age.
        age = (now.year - b.year) - ((now.month, now.day) < (b.month, b.day))
        # Statement
        if age < 18 or age > 65:
            raise forms.ValidationError('Denied ! Age must be between 18 and 65.')
        return birth
    
    # 8) Prevent FUTURES dates (card 3 and card 4)
    # A) College
    def clean_started_course(self):
        started_course = self.cleaned_data['started_course']
        if started_course > datetime.date.today():
             raise forms.ValidationError('Future date is invalid.')
        return started_course
    
    def clean_finished_course(self):
        finished_course = self.cleaned_data['finished_course']
        if finished_course > datetime.date.today():
             raise forms.ValidationError('Future date is invalid.')
        return finished_course
    
    # B) JOB
    def clean_started_job(self):
        started_job = self.cleaned_data['started_job']
        if started_job > datetime.date.today():
             raise forms.ValidationError('Future date is invalid.')
        return started_job
    
    def clean_finished_job(self):
        finished_job = self.cleaned_data['finished_job']
        if finished_job > datetime.date.today():
             raise forms.ValidationError('Future date is invalid.')
        return finished_job
    

# ===================== SEND EMAIL TO CANDIDATES ========================|
class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget= forms.Textarea)
    class Meta:
        fields = "__all__"