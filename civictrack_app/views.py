from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report, Comment
import json


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        image = request.FILES.get('image')

        Report.objects.create(
            title=title,
            description=description,
            location=location,
            latitude=float(latitude) if latitude else None,
            longitude=float(longitude) if longitude else None,
            image=image
        )

        messages.success(request, "Report submitted successfully!")
        return redirect('/')

    reports = Report.objects.all().order_by('-created_at')

    report_data = [
        {
            'title': r.title,
            'description': r.description,
            'lat': r.latitude,
            'lng': r.longitude,
        }
        for r in reports if r.latitude and r.longitude
    ]

    return render(request, 'civictrack/home.html', {
        'reports': reports,
        'report_data': json.dumps(report_data)
    })


# 👇 ADD THIS HERE
def add_comment(request, report_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        report = Report.objects.get(id=report_id)

        Comment.objects.create(
            report=report,
            text=text
        )

    return redirect('/')