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


class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, choices=SMOKER, default="")
    email = models.EmailField(max_length=50)
    message = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default="Pending")
    # Multiple checkboxes
    frameworks = MultiSelectField(choices=FRAMEWORKS, default=[], max_length=255)
    languages = MultiSelectField(choices=LANGUAGES, default=[], max_length=255)
    databases = MultiSelectField(choices=DATABASES, default=[], max_length=255)
    libraries = MultiSelectField(choices=LIBRARIES, default=[], max_length=255)
    mobile = MultiSelectField(choices=MOBILE, default=[], max_length=255)
    others = MultiSelectField(choices=OTHERS, default=[], max_length=255)

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
    