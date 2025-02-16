from django.shortcuts import render
from .models import Job

def alljobs(request):
    jobs = Job.objects
    return render(request, 'job/all-jobs.html', {'jobs':jobs})

# def detail(request, job_id):
#     detailJob = get_object_or_404(Job, pk=job_id)
#     return render(request, 'job/detail.html', {'job':detailJob})