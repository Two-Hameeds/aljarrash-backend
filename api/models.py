from django.db import models

# Create your models here.
from django.db import models
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)

class Client(models.Model):
    phone = models.CharField(max_length=13, primary_key=True, blank=False)
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        if self.name == None:
            return ""
        return self.name

class ProjectTypes(models.TextChoices):
    Destruction = 'destruction'
    Restoration = 'restoration'
    AddFloors = 'add_floors'
    Addition = 'addition'
    New = 'new'
    
class UseTypes(models.TextChoices):
    Entertaining = 'entertaining'
    Agricultural = 'agricultural'
    ResidentialCommercial = 'residential_commercial'
    Commercial = 'commercial'  
    Residential = 'residential'


class Status(models.TextChoices):
    Working_on_it = 'Working on it'
    Done = 'Done'
    Hold = 'Hold'
    Not_required = "Not required"

class DesignStatus(models.TextChoices):
    Ground = "Ground floor"
    First = "First floor"
    Second = "Second floor"
    Third = "Third floor"
    Annex = "Annex room"
    Facade = "Facade"

class FollowUpTypes(models.TextChoices):
    Paper = "Paper"
    Municipal = "Municipal"

class StructuralReviewStatus(models.TextChoices):
    Working_on_it = 'Working on it'
    Done = 'Done'


class Stages(models.TextChoices):
    Sketch = 'sketch'
    Sketch_Review = 'sketch_review'
    Approval_Before_Columns = 'approval_before_columns'
    Awaiting_Client_Approval = 'awaiting_client_approval'
    Execution_Stage = 'execution_stage'
    AutoCAD_Review = 'autocad_review'
    Ready_to_Print = 'ready_to_print'
    Validate_Sign_Review_Copy = 'validate_sign_review_copy'
    Ready_to_Collect = 'ready_to_collect'
    Client_Received_Copy = 'client_received_copy'
    Edit_Client_Notes = 'edit_client_notes'
    License_Issuance = 'license_issuance'
    Ready_for_Final_Receipt = 'ready_for_final_receipt'
    Completed_Projects = 'completed_projects'
    Inactive_Projects = 'inactive_projects'



class Project(models.Model):
    # essential info
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(Client, to_field='phone', on_delete=models.CASCADE, related_name='projects', null=False, blank=False)
    project_type = models.CharField(max_length=100, choices=ProjectTypes.choices, null=False, blank=False)
    use_type = models.CharField(max_length=100, choices=UseTypes.choices, null=False, blank=False)

    current_stage = models.CharField(max_length=100, choices=Stages.choices, null=False, blank=False)
    
    # stages info
    previous_stage = models.CharField(max_length=100, choices=Stages.choices, null=True, blank=True)
    
    sketch_start_time = models.DateTimeField(null=True, blank=True) # stage 1 entrance
    sketch_end_time = models.DateTimeField(null=True, blank=True) # stage 1 exit
    
    sketch_review_start_time = models.DateTimeField(null=True, blank=True) # stage 2 entrance
    sketch_review_end_time = models.DateTimeField(null=True, blank=True) # stage 2 exit
    
    awaiting_client_approval_start_time = models.DateTimeField(null=True, blank=True) # stage 3 entrance
    awaiting_client_approval_end_time = models.DateTimeField(null=True, blank=True) # stage 3 exit
    
    execution_stage_start_time = models.DateTimeField(null=True, blank=True) # stage 4 entrance
    execution_stage_end_time = models.DateTimeField(null=True, blank=True) # stage 4 exit
    
    autocad_start_time = models.DateTimeField(null=True, blank=True) # stage 5 entrance
    autocad_end_time = models.DateTimeField(null=True, blank=True) # stage 5 exit
    
    ready_to_print_start_time = models.DateTimeField(null=True, blank=True) # stage 6 entrance
    ready_to_print_end_time = models.DateTimeField(null=True, blank=True) # stage 6 exit
    
    validate_sign_review_copy_start_time = models.DateTimeField(null=True, blank=True) # stage 7 entrance
    validate_sign_review_copy_end_time = models.DateTimeField(null=True, blank=True) # stage 7 exit
    
    ready_to_collect_start_time = models.DateTimeField(null=True, blank=True) # stage 8 entrance
    ready_to_collect_end_time = models.DateTimeField(null=True, blank=True) # stage 8 exit
    
    client_received_copy_start_time = models.DateTimeField(null=True, blank=True) # stage 9 entrance
    client_received_copy_end_time = models.DateTimeField(null=True, blank=True) # stage 9 exit
    
    edit_client_notes_start_time = models.DateTimeField(null=True, blank=True) # stage 10 entrance
    edit_client_notes_end_time = models.DateTimeField(null=True, blank=True) # stage 10 exit
    
    license_issuance_start_time = models.DateTimeField(null=True, blank=True) # stage 11 entrance
    license_issuance_end_time = models.DateTimeField(null=True, blank=True) # stage 11 exit
    
    ready_for_final_receipt_start_time = models.DateTimeField(null=True, blank=True) # stage 12 entrance
    ready_for_final_receipt_end_time = models.DateTimeField(null=True, blank=True) # stage 12 exit
    
    completed_projects_start_time = models.DateTimeField(null=True, blank=True) # stage 13 entrance
    completed_projects_end_time = models.DateTimeField(null=True, blank=True) # stage 13 exit
    
    inactive_projects_start_time = models.DateTimeField(null=True, blank=True) # stage 14 entrance
    inactive_projects_end_time = models.DateTimeField(null=True, blank=True) # stage 14 exit
    
    
    
    

    design_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='designer', null=True, blank=True)
    contract_sign_date = models.DateField(null=True, blank=True)
    land_number = models.CharField(max_length=100, null=True, blank=True)
    plan_number = models.CharField(max_length=100, null=True, blank=True)
    land_area = models.FloatField(null=True, blank=True)
    project_location = models.CharField(max_length=100, null=True, blank=True)
    floors_number = models.IntegerField(null=True, blank=True)
    facades_number = models.IntegerField(null=True, blank=True)
    project_receipt_date = models.DateField(null=True, blank=True)
    sketch_approval_date = models.DateField(null=True, blank=True)
    columns_approval_date = models.DateField(null=True, blank=True)
    obstacles = models.CharField(max_length=100, null=True, blank=True)
    
    # sensetive fields
    s_project_value = models.FloatField(null=True, blank=True)
    s_first_payment = models.FloatField(null=True, blank=True)
    s_first_payment_date = models.DateField(null=True, blank=True)
    s_second_payment = models.FloatField(null=True, blank=True)
    s_second_payment_date = models.DateField(null=True, blank=True)
    s_third_payment = models.FloatField(null=True, blank=True)
    s_third_payment_date = models.DateField(null=True, blank=True)
    s_first_payment_stage = models.CharField(max_length=100, null=True, blank=True)
    s_second_payment_stage = models.CharField(max_length=100, null=True, blank=True)
    s_third_payment_stage = models.CharField(max_length=100, null=True, blank=True)
    s_modification_price = models.FloatField(null=True, blank=True)
    
    architecture_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    architect = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='architect', null=True, blank=True)
    architect_start_date = models.DateField(null=True, blank=True)
    architect_end_date = models.DateField(null=True, blank=True)
    architect_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    construction_status = models.CharField(max_length=100, null=True, blank=True)
    construction_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL,related_name='contruction_engineer', null=True, blank=True)
    construction_start_date = models.DateField(null=True, blank=True)
    construction_end_date = models.DateField(null=True, blank=True)
    construction_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    plumbing_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    plumbing_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='plumbing_engineer', null=True, blank=True)
    plumbing_start_date = models.DateField(null=True, blank=True)
    plumbing_end_date = models.DateField(null=True, blank=True)
    plumbin_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    electrical_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    electrical_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='electrical_engineer', null=True, blank=True)
    electrical_start_date = models.DateField(null=True, blank=True)
    electrical_end_date = models.DateField(null=True, blank=True)
    electrical_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    architecture_review = models.CharField(max_length=255, null=True, blank=True)
    architecture_reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='architecture_reviewer', null=True, blank=True)
    construction_review = models.CharField(max_length=255, null=True, blank=True)
    construction_reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='construction_reviewer', null=True, blank=True)
    plumbing_review = models.CharField(max_length=255, null=True, blank=True)
    plumbing_reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='plumbing_reviewer', null=True, blank=True)
    electrical_review = models.CharField(max_length=255, null=True, blank=True)
    electrical_reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='electrical_reviewer', null=True, blank=True)
    client_received_review_copy_date = models.DateField(null=True, blank=True)
    received_review_copy_from_client_date = models.DateField(null=True, blank=True)
    architecture_notes = models.CharField(max_length=255, null=True, blank=True)
    noted_fields = models.CharField(max_length=100, null=True, blank=True)
    corrector = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='corrector', null=True, blank=True)
    corrector_date = models.DateField(null=True, blank=True)
    receive_final_copy_date = models.DateField(null=True, blank=True)

    # typeof_follow_up = models.CharField(max_length=100, choices=FollowUpTypes.choices, null=True, blank=True)
    investor_affiliation = models.CharField(max_length=100,null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sketch_design_progress_status = models.CharField(max_length=100, choices=DesignStatus.choices, null=True, blank=True)
    plan_delivery_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(null=True, blank=True)
    moved_at = models.DateTimeField(null=True, blank=True)

    

    def __str__(self):
        if self.project_name == None:
            return ""
        return self.project_name
    
class AttachmenTypes(models.TextChoices):
    Contract = 'contract'
    Deed = 'deed'
    Report = 'report'
    Identity = 'identity'
    ContainerContract = 'container_contract'
    License = 'license'
    Plan = 'plan'
    LoadBearingCertificate = 'load_bearing_certificate'
    LocationCertificate = 'location_certificate'
    LandSurvey = 'land_survey'
    SoilTest = 'soil_test'
    CoordinateCertificate = 'coordinate_certificate'
    TechnicalReport = 'technical_report'
    DemolitionLetters = 'demolition_letters'
    Autocad = 'autocad'
    ClientForm = 'client_form'
    OldLicense = 'old_license'
    CivilDefense = 'civil_defense'
    WaterAuthority = 'water_authority'
    Other = 'other'

@deconstructible
class PathAndRename:
    def __call__(self, instance, filename):
        return f'static/attachments/{instance.type}s/{filename}'
    
class Attachment(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, choices=AttachmenTypes.choices, null=False, blank=False)
    attachment = models.FileField(upload_to=PathAndRename(), null=False, blank=False)
    uploaded_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_for = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.title == None:
            return ""
        return self.title

class Comment(models.Model):
    # title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    written_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to="static/attachments/", null=True, blank=True)
    written_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    written_for = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    # def __str__(self):
    #     if self.title == None:
    #         return ""
    #     return self.title
    
class TableView(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    stage = models.CharField(max_length=100, choices=Stages.choices, null=False, blank=False)
    view = models.JSONField(null=True, blank=True)

class BaladyStages(models.TextChoices):
    new_construction_license = 'new_construction_license'
    working_on_it = 'working_on_it'
    incomplete_or_requirements_are_unclear = 'incomplete_or_requirements_are_unclear'
    temporarly_stopped_or_technical_issues = 'temporarly_stopped_or_technical_issues'
    ready_for_pickup = 'ready_for_pickup'

class BaladyProject(models.Model):
    stage = models.CharField(max_length=100, choices=BaladyStages.choices, null=False, blank=False)

    project_name = models.CharField(max_length=100, null=False, blank=False)
    request_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    client_phone = models.ForeignKey(Client, to_field='phone', on_delete=models.CASCADE, related_name='balady_projects', null=False, blank=False)
    architecture_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    construction_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    plumbing_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    electrical_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    design_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='designer_balady', null=True, blank=True)
    columns_approval_date = models.DateField(null=True, blank=True)
    sketch_approval_date = models.DateField(null=True, blank=True)
    investor_affiliation = models.CharField(max_length=100, null=True, blank=True)
    project_receipt_date = models.DateField(null=True, blank=True)
    project_type = models.CharField(max_length=100, choices=ProjectTypes.choices, null=True, blank=True)
    land_number = models.CharField(max_length=100, null=True, blank=True)
    land_area = models.FloatField(null=True, blank=True)
    project_location = models.CharField(max_length=100, null=True, blank=True)
    project_number = models.CharField(max_length=100, null=True, blank=True)
    sketch_progress = models.CharField(max_length=100, null=True, blank=True)
    construction_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL,related_name='contruction_engineer_balady', null=True, blank=True)
    construction_start_date = models.DateField(null=True, blank=True)
    construction_review = models.CharField(max_length=255, null=True, blank=True)
    construction_end_date = models.DateField(null=True, blank=True)
    electrical_start_date = models.DateField(null=True, blank=True)
    electrical_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='electrical_engineer_balady', null=True, blank=True)
    electrical_end_date = models.DateField(null=True, blank=True)
    architect_start_date = models.DateField(null=True, blank=True)
    architect_end_date = models.DateField(null=True, blank=True)
    plumbing_start_date = models.DateField(null=True, blank=True)
    plumbing_end_date = models.DateField(null=True, blank=True)
    plan_delivery_date = models.DateField(null=True, blank=True)
 
    