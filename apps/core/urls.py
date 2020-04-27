from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search-results/', views.search_results, name='search_results'),
    path('detailed_search_results/<job_id>/', views.detailed_search_results, name='detailed_search_results'),
    path('saved_jobs/<user_name>/', views.saved_jobs, name='saved_jobs'),
    path('save_job/<job_id>/<user_name>/', views.save_job, name='save_job')

]
