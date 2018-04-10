from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import Project
from django.forms.widgets import SelectDateWidget



class UserRegisterForm(UserCreationForm):
    class Meta():
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #custom label for field
        self.fields['username'].label = 'User Name'


class IndexForm(ModelForm):
    class Meta():
        model = Project
        fields = ('project_name', 'is_complete', 'is_approved' )

class AdminForm(ModelForm):
    class Meta():
        model = Project
        fields = ('project_name', 'review_type')

class ProjectForm(ModelForm):
    class Meta():
        model = Project
        fields = ('project_name', 'review_type', 'consent_form', 'assent_form', 'surveys_form', 'methodology_form', 'grant_proposal_form', 'ext_circumstances_form',
                  'principal_investigator_signature', 'faculty_supervisor_signature', 'funding', 'start_date', 'end_date', 'purpose', 'methodology', 'benefits',
                  'risk', 'recruited', 'why_identify', 'how_data_store', 'consent_process')

        widgets = {'start_date' : SelectDateWidget, 'end_date' : SelectDateWidget, 'funding' : forms.Textarea(attrs={'placeholder' : 'Source of Funding (if any):'}),
                    'purpose' : forms.Textarea(attrs={'placeholder' : 'Describe the Scientific Purpose of the Investigation'}),
                    'methodology' : forms.Textarea(attrs={'placeholder' : 'Describe the research methodology in non-technical language (the IRB needs to know what will be done with or to all research participants)'}),
                    'benefits' : forms.Textarea(attrs={'placeholder' : 'What are the potential benefits of this research (either directly to the participants, or to the body of knowledge being researched)'}),
                    'risk' : forms.Textarea(attrs={'placeholder' : 'What are the anticipated risks (risks include, physical, psychological, or economic harm; be certain to describe the steps taken to protect participants from these risks)'}),
                    'recruited' : forms.Textarea(attrs={'placeholder' : 'Describe how participants will be recruited (must include total number and age of all participants to be recruited and any compensation participants will be provided)'}),
                    'why_identify' : forms.Textarea(attrs={'placeholder' : 'Describe why it is necessary that the Primary Investigator(s) and/or Supervisor know the identity of the participants (not  for Exempt Reviews)'}),
                    'how_data_store' : forms.Textarea(attrs={'placeholder' : 'Describe how data collected for this project will be securely stored and how and when it will be destroyed'}),
                    'consent_process' : forms.Textarea(attrs={'placeholder' : 'Describe the informed consent process'}),
                    'review_notes' : forms.Textarea(attrs={'placeholder' : 'Add your notes for this submission here'})}

# Clone of ProjectForm + review_notes
class ProjectReviewForm(ModelForm):
    class Meta():
        model = Project
        fields = ('project_name', 'review_type', 'consent_form', 'assent_form', 'surveys_form', 'methodology_form', 'grant_proposal_form', 'ext_circumstances_form',
                  'principal_investigator_signature', 'faculty_supervisor_signature', 'funding', 'start_date', 'end_date', 'purpose', 'methodology', 'benefits',
                  'risk', 'recruited', 'why_identify', 'how_data_store', 'consent_process', 'review_notes')

        widgets = { 'review_notes' : forms.Textarea(attrs={'placeholder' : 'Add your notes for this project here.'})}
