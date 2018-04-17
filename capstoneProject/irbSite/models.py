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
    project_name = models.CharField(max_length = 20, unique = True)
    last_modified = models.DateField(auto_now=True, blank = True)

    # project qualified for
    REVIEW_TYPE = (
        ('exempt review' , 'Exempt Review'),
        ('expedited review', 'Expedited Review'),
        ('full irb review', 'Full IRB Review'),)
    review_type = models.CharField(max_length = 20, choices = REVIEW_TYPE, blank = True)

    # https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/
    consent_form = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    assent_form = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    surveys_form = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    methodology_form = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    grant_proposal_form = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    ext_circumstances_form = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    principal_investigator_signature = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    faculty_supervisor_signature = models.FileField(blank = True, null=True, upload_to="forms/%Y/%m/%D/")
    funding = models.CharField(max_length = 500, blank = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    purpose = models.CharField(max_length = 500, blank = True )
    methodology = models.CharField(max_length = 500, blank = True )
    benefits = models.CharField(max_length = 500, blank = True )
    risk = models.CharField(max_length = 500, blank = True )
    recruited = models.CharField(max_length = 500, blank = True )
    why_identify = models.CharField(max_length = 500, blank = True )
    how_data_store = models.CharField(max_length = 500, blank = True )
    consent_process = models.CharField(max_length = 500, blank = True )
    review_notes = models.CharField(max_length = 500, blank = True)
    date_submitted = models.DateField(auto_now_add = True)
    is_complete = models.BooleanField(default = False,blank = True)
    is_approved = models.BooleanField(default = False, blank = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
