from django.shortcuts import render
import requests
from django.shortcuts import redirect
from .models import Saved_Job

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

# # def search_results(request):
# #     context = {
# #     }

# #     return render(request, 'pages/search_results.html', context)

#     return render(request, 'news.html', context)


def search_results(request):
    search_query = request.GET['searchterm']
    search_location = request.GET['searchlocation']

    context = {
        'result_count': 0,
        'search_term': search_query,
        'search_location': search_location,

     }

    context['results_count'] = 0

    url = 'https://jobs.github.com/positions.json?'
    url += 'description=' + search_query
    url += '&location=' + search_location

    response = requests.get(url)
    results_data = response.json()
    job_list =[]
    for result in results_data:
        job_list.append(result)
    

    context['job_results'] = job_list
    

    return render(request, 'pages/search_results.html', context)
    
   
def detailed_search_results(request,job_id):
    
    url = f'https://jobs.github.com/positions/{job_id}.json'
 
    response = requests.get(url)
    results_data = response.json()
    request.session[job_id] = results_data

    context = {'job': results_data}

    return render(request, 'pages/detailed_search_results.html', context)


def saved_jobs(request,user_name):
    s_jobs = Saved_Job.objects.filter(username=user_name).order_by('-created')

    context = {
            'saved_jobs' : s_jobs
        }

    return render(request, 'pages/saved_jobs.html', context)

def save_job(request, job_id ,user_name):
    job_data = request.session.get(job_id, None)
    Saved_Job.objects.create(
        job_id=job_data['id'],
        job_title=job_data['title'],
        job_description=job_data['description'],
        applied=False,
        username=user_name,
        company_url=job_data['company_url']
    )
    return redirect("/saved_jobs/" + user_name)


def apply_job(request, job_id ,user_name):
    
    # U in CRUD
    saved_job = Saved_Job.objects.filter(job_id=job_id).first()
    job_url = ""
    # if job already exists
    if saved_job is not None:
        saved_job.applied = True
        job_url = saved_job.company_url
        saved_job.save()
    # if job does not already exist
    else:
        job_data = request.session.get(job_id, None)
        Saved_Job.objects.create(
            job_id=job_data['id'],
            job_title=job_data['title'],
            job_description=job_data['description'],
            company_url=job_data['company_url'],
            applied=True,
            username=user_name
        )
        job_url = job_data['company_url']
    
    return redirect(job_url)
    


# # U in CRUD
# job = Saved_Job.objects.get(id=job_id)
# job.applied = True
# job.save()

# #return redirect(job_data.company_url)  # Once you add company_url
# return redirect('/saved_jobs/' + request.user.username)
