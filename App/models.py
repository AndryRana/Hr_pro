from django.db import models
from multiselectfield import MultiSelectField

SITUATION = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
)

PERSONALITY = (
    ("", "Select a personality"),
    ("I am outgoing", "I am outgoing"),
    ("I am sociable", "I am sociable"),
    ("I am antisocial", "I am antisocial"),
    ("I am discreet", "I am discreet"),
    ("I am serious", "I am serious"),
)

SMOKER = (
    ("1", "Yes"),
    ("2", "No"),
)

# Multiple checkboxes
FRAMEWORKS = (
    ("Laravel", "Laravel"),
    ("Angular", "Angular"),
    ("Django", "Django"),
    ("Flask", "Flask"),
    ("Vue", "Vue"),
    ("Others", "Others"),
)
LANGUAGES = (
    ("Python", "Python"),
    ("Javascript", "Javascript"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("Ruby", "Ruby"),
    ("Others", "Others"),
)
DATABASES = (
    ("MySql", "MySql"),
    ("Postgree", "Postgree"),
    ("MongoDB", "MongoDB"),
    ("SqLite3", "SqLite3"),
    ("Oracle", "Oracle"),
    ("Others", "Others"),
)
LIBRARIES = (
    ("Ajax", "Ajax"),
    ("Jquery", "Jquery"),
    ("ReactJs", "ReactJs"),
    ("Chart.js", "Chart.js"),
    ("Gsap", "Gsap"),
    ("Others", "Others"),
)
MOBILE = (
    ("React native", "React native"),
    ("Kivy", "Kivy"),
    ("Flutter", "Flutter"),
    ("Ionic", "Ionic"),
    ("Xamarin", "Xamarin"),
    ("Others", "Others"),
)
OTHERS = (
    ("UML", "UML"),
    ("SQL", "SQL"),
    ("Docker", "Docker"),
    ("GIT", "GIT"),
    ("GraphQL", "GraphQL"),
    ("Others", "Others"),
)

# Education
STATUS_COURSE = (
    ("", "Select your status"),
    ("I'm studying", "I'm studying"),
    ("I took a break", "I took a break"),
    ("Completed", "Completed"),
)

class Candidate(models.Model):
    # PERSONAL (CARD 1)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5, verbose_name="Job code")
    # age = models.CharField(max_length=3)
    birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Birthday")
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50, verbose_name="Salary expectation")
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, choices=SMOKER, default="")
    email = models.EmailField(max_length=50)
    message = models.TextField(verbose_name="Presentation")
    file = models.FileField(upload_to='resume', blank=True, verbose_name="Resume")
    image = models.ImageField(upload_to='photo', blank=True, verbose_name="Photo")
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default="Pending")
    company_note = models.TextField(blank=True)
    # SKILLS(CARD 2) Multiple checkboxes
    frameworks = MultiSelectField(choices=FRAMEWORKS, max_length=50)
    languages = MultiSelectField(choices=LANGUAGES, max_length=50)
    databases = MultiSelectField(choices=DATABASES, max_length=50)
    libraries = MultiSelectField(choices=LIBRARIES, max_length=50)
    mobile = MultiSelectField(choices=MOBILE, max_length=50)
    others = MultiSelectField(choices=OTHERS, max_length=50)
    # EDUCATION (CARD 3)
    institution = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    started_course = models.DateField(auto_now_add=False)
    finished_course = models.DateField(blank=True,null=True, auto_now_add=False)
    about_course=models.TextField()
    status_course= models.CharField(max_length=50,null=True, choices=STATUS_COURSE)
    #PROFESSIONAL (CARD 4)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    started_job = models.DateField(blank=True,null=True,auto_now_add=False)
    finished_job= models.DateField(blank=True,null=True,auto_now_add=False)
    about_job=models.TextField()
    employed = models.BooleanField(null=True,verbose_name='I am employed')
    remote = models.BooleanField(null=True,verbose_name='I agree to work remotely')
    travel = models.BooleanField(null=True,verbose_name='I am available for travel')
    
    
    # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname

    # Concatenate F-name and L-name (Admin table)
    def name(obj):
        return "%s %s" % (obj.firstname, obj.lastname)
    
    # Concatenate (When you clicking over the candidates)
    def __str__(self):
        return self.firstname + " " + self.lastname
    
# --------------------- SEND EMAIL ------------------------|
    
class Email(models.Model):
    # Hidden
    employee = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=50)
    
    # Not hidden
    subject = models.CharField(max_length=50)
    message = models.TextField()
    # Get DateTime the email was sent
    sent_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
# --------------------- CHATBOX------------------------|
# About Candidates
class Chat_candidate(models.Model):
    candidate_email = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    chat = models.CharField(max_length=500)
    dt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user