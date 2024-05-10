from django.urls import path
from .views import HomePage, ResumePage, PortfolioPage, ContactPage

app_name = 'home'
urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
    path("resume/", ResumePage.as_view(), name="resume_page"),
    path("portfolio/", PortfolioPage.as_view(), name="portfolio_page"),
    path("contact/", ContactPage.as_view(), name="contact_page"),
]