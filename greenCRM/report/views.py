from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import matplotlib.pyplot as plt
import numpy as np
from django.contrib.auth.decorators import login_required
from .models import Report
from .models import Client

@login_required
def report_list(request):
    reports = Report.objects.filter(created_by=request.user)
    
    return render(request, 'report/report_list.html', {
        'reports': reports,
    })

def report(request):
    clients = Client.objects.filter(created_by=request.user)
    # Generate the chart using matplotlib

    x = [client.org_name for client in clients]
    y = [client.total_order_value for client in clients]
    fig, ax = plt.subplots()
    ax.bar(x, y)
    chart_data = BytesIO()
    fig.savefig(chart_data, format='png')
    chart_data.seek(0)

    # Render the HTML template
    template = get_template('report.html')
    context = {'chart_data': chart_data}
    html = template.render(context)

    # Export the report as a PDF
    pdf_data = BytesIO()
    pisa.CreatePDF(html, dest=pdf_data)
    pdf_data.seek(0)

    # Return the PDF as an HTTP response
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response
