import requests
from django.shortcuts import render

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

def search_results(request):
    search_query = request.GET['searchterm']

    context = {
        'result_count': 0,
        'search_term': search_query,
     }

    context['results_count'] = 0

    url = 'https://jobs.github.com/positions.json?location=bay+area&description='
    url += search_query

    response = requests.get(url)
    results_data = response.json()
    job_list =[]
    for result in results_data:
        job_list.append(result)
    

    context['job_results'] = job_list
    

    return render(request, 'pages/search_results.html', context)

def detailed_search_results(request):
    context = {
    }

    return render(request, 'pages/detailed_search_results.html', context)

def saved_jobs(request):
    context = {
    }

    return render(request, 'pages/saved_jobs.html', context)
