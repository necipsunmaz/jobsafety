from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from jobsafety.settings import CITIES


class Team(models.Model):
    manager = models.ForeignKey(User)
    name = models.CharField(verbose_name=_("Team Name"), max_length=250)
    address = models.TextField(verbose_name=_("Team Address"))

    def __str__(self):
        return self.manager.username


class TeamUser(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    job = models.CharField(verbose_name=_("Expert Job"), max_length=255)
    company = models.CharField(verbose_name=_("Expert Company"), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Company(models.Model):
    name = models.CharField(verbose_name=_("Company Name"), max_length=255)
    address = models.TextField(verbose_name=_("Company Adress"))
    number = models.CharField(verbose_name=_("Telephone Number"), max_length=11, blank=True)
    fax = models.CharField(verbose_name=_("Fax Number"), max_length=11, blank=True)
    email = models.EmailField(verbose_name=_("Company E-mail"), max_length=150)
    country = models.CharField(choices=CITIES, verbose_name=_("Company City"), max_length=85, blank=True)
    website = models.CharField(verbose_name=_("Company Site"), max_length=80, blank=True)

    def __str__(self):
        return self.name

"""
class Analysis(models.Model):
    team = models.ForeignKey(Team)
    company = models.ForeignKey(Company)
"""