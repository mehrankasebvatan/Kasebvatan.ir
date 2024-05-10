from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = "home/index.html"


class ContactPage(TemplateView):
    template_name = "home/contact.html"


class ResumePage(TemplateView):
    template_name = "home/resume.html"


class PortfolioPage(TemplateView):
    template_name = "home/portfolio.html"
