from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

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
                'style':'font-size: 13px; text-transform: uppercase'
        })
    )
    
    # Email code  (Uppercase Function)
    email = Lowercase(
        label='Email address', 
        min_length=8, max_length=50, 
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+(\.[a-zA-Z]{2,4})+$', 
        message="Put a valid email address!")], 
        widget=forms.TextInput(attrs={
            'placeholder':'Email',
            'style':'font-size: 13px; text-transform: lowercase'
        }),
        
    )
    
    # Method 1
    # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    
    # Method 2
    age = forms.CharField(
        label='Your age', min_length=2, max_length=2, 
        validators= [RegexValidator(r'^[0-9]*$', 
        message="Only numbers is allowed!")], 
        widget=forms.TextInput(attrs={
            'placeholder':'Age',
            'style':'font-size: 13px;'
        }),
        
    )
    
    #Experience
    experience = forms.BooleanField(label="I have experience", required = False)
    
    #Message
    message =  forms.CharField(
        label='About you', min_length=50, max_length=1000,
        required=False, 
        widget=forms.Textarea(
            attrs={
                'placeholder':'Talk a little about you',
                'rows':5,
                'style':'font-size: 13px;'
            }
        ),
    )
    
    # File (Upload)
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'style':'font-size: 13px;'
            }
        )
    )
    
    # Method 1 (Gender)
    #GENDER = [('M','Male'), ('F', 'Female')]
    #gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))
    
    class Meta:
        model = Candidate
        #fields = "__all__"
        exclude =['created_at','Situation'] 
        #fields = ['firstname', 'lastname', 'email', 'message','age' ] 
        
        # Label_control
        #labels = {
        #    'gender': 'Your Gender',
        #    'smoker': 'Do you smoke ?',
        #}
        
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
            #Phone
            'phone': forms.TextInput(
                attrs={
                    'style':'font-size:13px',
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
            'personality':forms.Select(attrs={'style':'font-size: 13px;'})
        }
        
    # ------------------------------------------ SUPER FUNCTION--------------------------------|
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        
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
        
        # ============ ADVANCED CONTROL PANEL (multiple input )READONLY / DISABLED BY 'LOOP FOR' IN [ARRAY]============|
        # 1) readonly
        #readonly = ['firstname', 'lastname','job','email', 'age', 'phone']
        #for field in readonly:
         #   self.fields[field].widget.attrs['readonly'] = 'true'
            
        # 2) Disabled
        #disabled= ['personality', 'salary','gender','smoker', 'experience']
        #for field in disabled:
        #    self.fields[field].widget.attrs['disabled'] = 'true'
        
    # ------------------------------------------END // SUPER FUNCTION-----------------------------------|
        
    # FUNCTION TO PREVENT DUPLICATED ENTRIES
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
        