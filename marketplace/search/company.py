from company.models import Company


def search_company(search_text):
    qs = Company.objects.all()

def order