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
    context = {
    }

    return render(request, 'pages/search_results.html', context)

def detailed_search_results(request):
    context = {
    }

    return render(request, 'pages/detailed_search_results.html', context)

def saved_jobs(request):
    context = {
    }

    return render(request, 'pages/saved_jobs.html', context)
