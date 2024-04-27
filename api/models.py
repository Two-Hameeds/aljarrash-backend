from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)

class Client(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        if self.name == None:
            return ""
        return self.name

class ProjectTypes(models.TextChoices):
    New = 'new'
    Addition = 'addition'
    Restoration = 'restoration'

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
    Sketch = '1'
    Sketch_Review = '2'
    Awaiting_Client_Approval = '3'
    Execution_Stage = '4'
    AutoCAD_Review = '5'
    Ready_to_Print = '6'
    Validate_Sign_Review_Copy = '7'
    Ready_to_Collect = '8'
    Client_Received_Copy = '9'
    Edit_Client_Notes = '10'
    License_Issuance = '11'
    Ready_for_Final_Receipt = '12'
    Completed_Projects = '13'
    Inactive_Projects = '14'



class Project(models.Model):
    stage = models.CharField(max_length=100, choices=Stages.choices, null=False, blank=False)

    project_name = models.CharField(max_length=100, null=True, blank=True)
    # attachments
    _contract = models.FileField(upload_to="static/contracts/", null=True, blank=True)
    _deed = models.FileField(upload_to="static/deeds/", null=True, blank=True)
    _report = models.FileField(upload_to="static/reports/", null=True, blank=True)
    _identity = models.FileField(upload_to="static/identities/", null=True, blank=True)
    _container_contract = models.FileField(upload_to="static/container_contracts/", null=True, blank=True)
    _license = models.FileField(upload_to="static/old_licenses/", null=True, blank=True)
    _plan = models.FileField(upload_to="static/palns/", null=True, blank=True)
    _load_bearing_certificate=models.FileField(upload_to="static/load_bearing_certificates/", null=True, blank=True)
    _location_certificate=models.FileField(upload_to="static/location_certificates/", null=True, blank=True)
    _land_survey = models.FileField(upload_to="static/land_surveys/", null=True, blank=True)
    _soil_test = models.FileField(upload_to="static/soil_tests/", null=True, blank=True)
    _coordinate_certificate=models.FileField(upload_to="static/coordinate_certificates/", null=True, blank=True)
    _technical_report=models.FileField(upload_to="static/technical_reports/", null=True, blank=True)
    _demolition_letters=models.FileField(upload_to="static/demolition_letters/", null=True, blank=True)
    _autocad=models.FileField(upload_to="static/autocads/", null=True, blank=True)
    _client_form = models.FileField(upload_to="static/client_forms/", null=True, blank=True)
    _old_license = models.FileField(upload_to="static/old_licenses/", null=True, blank=True)
    _civil_defense = models.FileField(upload_to="static/civil_defenses/", null=True, blank=True)
    _water_authority = models.FileField(upload_to="static/water_authorities/", null=True, blank=True)


    design_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='designer', null=True, blank=True)
    client_number = models.ForeignKey(Client, on_delete=models.SET_NULL, related_name='client', null=True, blank=True)
    contract_sign_date = models.DateField(null=True, blank=True)
    project_type = models.CharField(max_length=100, choices=ProjectTypes.choices, null=True, blank=True)
    use_type = models.CharField(max_length=100, null=True, blank=True)
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
    project_value = models.FloatField(null=True, blank=True)
    first_payment = models.FloatField(null=True, blank=True)
    first_payment_date = models.DateField(null=True, blank=True)
    second_payment = models.FloatField(null=True, blank=True)
    second_payment_date = models.DateField(null=True, blank=True)
    third_payment = models.FloatField(null=True, blank=True)
    third_payment_date = models.DateField(null=True, blank=True)
    first_payment_stage = models.CharField(max_length=100, null=True, blank=True)
    second_payment_stage = models.CharField(max_length=100, null=True, blank=True)
    third_payment_stage = models.CharField(max_length=100, null=True, blank=True)
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
    correction_date = models.DateField(null=True, blank=True)
    receive_final_copy_date = models.DateField(null=True, blank=True)

    typeof_follow_up = models.CharField(max_length=100, choices=FollowUpTypes.choices, null=True, blank=True)
    investor_affiliation = models.BooleanField(null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sketch_design_progress_status = models.CharField(max_length=100, choices=DesignStatus.choices, null=True, blank=True)
    plan_delivery_date = models.DateField(null=True, blank=True)
    modification_price = models.FloatField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    moved_at = models.DateField(null=True, blank=True)

    

    def __str__(self):
        if self.project_name == None:
            return ""
        return self.project_name

class Comment(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    written_at = models.DateField(null=True, blank=True)
    attachment = models.FileField(upload_to="static/attachments/", null=True, blank=True)
    written_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    written_for = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.title == None:
            return ""
        return self.title
    
class TableView(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    stage = models.CharField(max_length=100, choices=Stages.choices, null=False, blank=False)
    view = models.JSONField(null=True, blank=True)

    