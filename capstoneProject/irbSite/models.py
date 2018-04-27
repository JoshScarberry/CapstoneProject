from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    #is_reviewer = models.BooleanField(default = False)
    def __str__(self):
        return "@{}".format(self.username)

#https://stackoverflow.com/questions/3641483/django-user-model-and-custom-primary-key-field
#class IRBuser(AbstractBaseUser, auth.models.PermissionMixin):
#    first_name = models.Charfield(max_length = 20)
#    last_name = models.Charfield(max_length = 20)
#    email = models.EmailField(max_length = 20, unique = True, primary_key = True)
#    password = Charfield(max_length = 20)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length = 50)
    last_modified = models.DateField(auto_now=True, blank = True)

    # project qualified for
    REVIEW_TYPE = (
        ('exempt review' , 'Exempt Review'),
        ('expedited review', 'Expedited Review'),
        ('full irb review', 'Full IRB Review'),)
    review_type = models.CharField(max_length = 20, choices = REVIEW_TYPE)

    consent_form = models.FileField(blank = True, null = True)
    assent_form = models.FileField(blank = True, null = True)
    surveys_form = models.FileField(blank = True, null = True)
    methodology_form = models.FileField(blank = True, null = True)
    grant_proposal_form = models.FileField(blank = True, null = True)
    ext_circumstances_form = models.FileField(blank = True, null = True)
    principal_investigator_signature = models.FileField(blank = True, null = True)
    faculty_supervisor_signature = models.FileField(blank = True, null = True)
    funding = models.CharField(max_length = 3000)
    start_date = models.DateField(blank = True)
    end_date = models.DateField(blank = True)
    purpose = models.CharField(max_length = 3000)
    methodology = models.CharField(max_length = 3000)
    benefits = models.CharField(max_length = 3000)
    risk = models.CharField(max_length = 3000, blank = True )
    recruited = models.CharField(max_length = 3000)
    why_identify = models.CharField(max_length = 3000)
    how_data_store = models.CharField(max_length = 3000)
    consent_process = models.CharField(max_length = 3000)
    review_notes = models.CharField(max_length = 3000, blank = True, null = True)
    date_approved = models.DateField(null = True)
    date_submitted = models.DateField(auto_now_add = True)

    COMPLETE_CHOICES = (
        (True, 'Yes'),
        (False, 'No, allow submitter to edit')
    )
    is_complete = models.BooleanField(default = True, choices = COMPLETE_CHOICES)

    APPROVED_CHOICES = (
        (False, 'Not Approved'),
        (True, 'Approved')
    )
    is_approved = models.BooleanField(default = False, choices = APPROVED_CHOICES)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
