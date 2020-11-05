from django.db import models
from .company import Company


class CompanyFiles(models.Model):
    company = models.OneToOneField(Company,
                                   on_delete=models.CASCADE,
                                   related_name='files',
                                   )
    picture = models.ImageField(upload_to='company_files/pictures', blank=True)
    banner = models.ImageField(upload_to='company_files/banners', blank=True)


class File(models.Model):
    company_files = models.ForeignKey(CompanyFiles,
                                          on_delete=models.CASCADE,
                                      related_name='files',
                                      )
    file = models.FileField(upload_to='company_files/files',null=True,blank=True)
    note = models.CharField(max_length=255, blank=True)


class Image(models.Model):
    company_files = models.ForeignKey(CompanyFiles,
                                      on_delete=models.CASCADE,
                                      related_name='images',
                                      )
    image = models.ImageField(upload_to='company_files/images')
