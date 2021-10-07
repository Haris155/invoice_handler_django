import uuid
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def create_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    file_name = uuid.uuid4()
    response['content-Disposition'] = f'filename="{file_name}.pdf"'

    template = get_template('home/test.html')
    html = template.render({"text": "hi this is haris"})

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def countDesigns(obj):
    paid = 0
    unpaid = 0
    for design in obj:
        if design.ispaid:
            paid += 1
        else:
            unpaid += 1
    return paid, unpaid