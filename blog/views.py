from django.views.generic import TemplateView


# Create your views here.
class BlogHomePage(TemplateView):
    template_name = "blog/index.html"
