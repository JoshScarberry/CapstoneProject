from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User




# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    #is_reviewer = models.BooleanField(default = False)
    def __str__(self):
        return "@{}".format(self.username)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length = 20)

    # https://stackoverflow.com/questions/31130706/dropdown-in-django-model
    # project qualifies for
    #REVIEW_TYPE = (
    #    ('exempt review', 'Exempt Review'),
    #    ('expedited review', 'Expedited Review'),
    #    ('full irb review', 'Full IRB Review'),
    #)
    #review_type = forms.CharField(max_length = 10, choices = REVIEW_TYPE)
    review_type = models.CharField(max_length = 10)

    # https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/
    consent_form = models.FileField()
    assent_form = models.FileField()
    surveys_form = models.FileField()
    methodology_form = models.FileField()
    grant_proposal_form = models.FileField()
    ext_circumstances_form = models.FileField()
    principal_investigator_signature = models.FileField()
    faculty_supervisor_signature = models.FileField()

    funding = models.CharField(max_length = 500)

    # https://stackoverflow.com/questions/16356289/how-to-show-datepicker-calendar-on-datefield
    #start_date = forms.DateField(widget = forms.TextInput(attrs =
    #                            {
    #                                'class' : 'datepicker'
    #                            }))
    #end_date = forms.DateField(widget = forms.TextInput(attrs =
    #                            {
    #                                'class' : 'datepicker'
    #                            }))

    start_date = models.DateField()
    end_date = models.DateField()

    purpose = models.CharField(max_length = 500 )
    methodology = models.CharField(max_length = 500 )
    benefits = models.CharField(max_length = 500 )
    risk = models.CharField(max_length = 500 )
    recruited = models.CharField(max_length = 500 )
    why_identify = models.CharField(max_length = 500 )
    how_data_store = models.CharField(max_length = 500 )
    consent_process = models.CharField(max_length = 500 )
    review_notes = models.CharField(max_length = 500)
    is_complete = models.BooleanField(default = False)
    is_approved = models.BooleanField(default = False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
