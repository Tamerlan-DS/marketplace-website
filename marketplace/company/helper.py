from .models import *


def create_company(owner, name):
    company = Company.objects.create(owner=owner)
    company.save()
    create_company_info(company, name)
    create_company_contacts(company)
    create_company_files(company)


def create_company_info(company, name):
    company_info = CompanyInfo.objects.create(company=company, name=name)
    company_info.save()


def create_company_contacts(company):
    company_contacts = CompanyContacts.objects.create(company=company)
    company_contacts.save()


def create_company_files(company):
    company_files = CompanyFiles.objects.create(company=company)
    company_files.save()

def add_news(news):
    news = News.objects.create(news=news)
    news.save()

def add_Review(Reviews):
    Review = Reviews.objects.create(Reviews=Reviews)
    Review.save()

def add_Services(Services):
    Services = Services.objects.create(Services=Services)
    Services.save()

def add_branches(branches):
    branches = branches.objects.create(branches=branches)
    branches.save()
