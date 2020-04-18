from django.conf import settings
from wkhtmltopdf.views import PDFTemplateResponse


def pdf_view(request, article,):
    template = 'blogapp/article_detail.html'
    context = {
        "object": article,
    }
    cmd_options = settings.WKHTMLTOPDF_CMD_OPTIONS

    return PDFTemplateResponse(request=request,
                               context=context,
                               template=template,
                               filename=f'{article.title}.pdf',
                               cmd_options=cmd_options)
