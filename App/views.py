from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Login required to access private pages
from django.views.decorators.cache import cache_control # Destroy the section after log out
from django.core.paginator import Paginator
from django.db.models import Q
# Concatenate (F-name and L-name)
from django.db.models.functions import Concat # Concatenate
from django.db.models import Value as P

#---------------------------- FRONTEND ---------------------------|
# Home
def home(request):
    return render(request, 'home.html')

# Candidate registration
def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Form sent successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "register.html", {'form': form})
    else:
        form = CandidateForm()
        return render(request, "register.html", {'form': form})
    
    
#---------------------------- BACKEND ---------------------------|
# HR - Home page (Backend)
@login_required(login_url="login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def backend(request):
    # Filter (individually)
    # if request.method == 'POST':
    #     job = request.POST.get('job')
    #     filter = Candidate.objects.filter(job=job)
    #     context = {
    #         'candidates':filter
    #     }
    #     return render(request, 'backend.html', context)
    
    # Global filter
    if request.method == 'POST':
        job = request.POST.get('job')
        gender = request.POST.get('gender')
        filter = Candidate.objects.filter(Q(job=job) | Q(gender=gender))
        context = {
            'candidates':filter
        }
        return render(request, 'backend.html', context)
    #Global search
    elif 'q' in request.GET:
        q = request.GET['q']
        all_candidate_list = Candidate.objects.annotate(
            name=Concat('firstname',P(' '),'lastname')).\
            filter(Q(name__icontains=q) | Q(firstname__icontains=q) | Q(lastname__icontains=q) |
            Q(email__icontains=q) | Q(phone__icontains=q)).order_by('-created_at')
    else:
        all_candidate_list = Candidate.objects.all().order_by('-created_at')
    #Pagination
    paginator = Paginator(all_candidate_list, 10)
    page = request.GET.get('page')
    all_candidate = paginator.get_page(page)
    context = {'candidates': all_candidate}
    return render(request, 'backend.html', context)   
        
# Access Candidates (individually)
@login_required(login_url="login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def candidate(request, id):
    candidate = Candidate.objects.get(pk =id)
    # form = CandidateForm(instance = data)
    # array =  ['experience','firstname','lastname','job','email','birth','phone','salary',
    #     'personality','gender','smoker','file','frameworks','languages','databases','libraries',
    #     'mobile','others','message','image','institution','about_course','course','status_course','started_course', 
    #     'finished_course','company','position','about_job','started_job', 'finished_job','employed','remote','travel']
    # for field in array:
    #     form.fields[field].disabled = True
    #     form.fields['file'].widget.attrs.update({'style':'display:none'})
    #     form.fields['image'].widget.attrs.update({'style':'display:none'})
    return render(request,'candidate.html', {'candidate':candidate})#, {'form':form}
