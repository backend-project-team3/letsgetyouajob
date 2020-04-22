from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search-results/', views.search_results, name='search_results'),
    path('detailed-search-results/', views.detailed_search_results, name='detailed_search_results'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
]
