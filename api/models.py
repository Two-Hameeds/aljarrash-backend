# Create your models here.
from django.db import models
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import AbstractUser

from .choices import (
    ProjectTypes,
    UseTypes,
    Status,
    DesignStatus,
    FollowUpTypes,
    StructuralReviewStatus,
    Stages,
    AttachmentTypes,
    BaladyStages,
    BaladyRequestTypes,
    LandSurveyStages,
    SortingDeedsStages,
)


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


class Project(models.Model):
    global_id = models.IntegerField(null=True, blank=True)
    # essential info
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        Client,
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="projects",
        null=False,
        blank=False,
    )
    project_type = models.CharField(
        max_length=100, choices=ProjectTypes.choices, null=False, blank=False
    )
    use_type = models.CharField(
        max_length=100, choices=UseTypes.choices, null=False, blank=False
    )

    stage = models.CharField(
        max_length=100, choices=Stages.choices, null=False, blank=False
    )


    # attachments
    required_attachments = models.JSONField(null=True, blank=True)

    design_eng = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="designer",
        null=True,
        blank=True,
    )
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
    s_payments = models.JSONField(null=True, blank=True, default=list)
    s_modification_price = models.FloatField(null=True, blank=True)
    s_history = models.JSONField(null=True, blank=True, default=list)

    architecture_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    architect = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="architect",
        null=True,
        blank=True,
    )
    architect_start_date = models.DateField(null=True, blank=True)
    architect_end_date = models.DateField(null=True, blank=True)
    architect_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    construction_status = models.CharField(max_length=100, null=True, blank=True)
    construction_eng = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="contruction_engineer",
        null=True,
        blank=True,
    )
    construction_start_date = models.DateField(null=True, blank=True)
    construction_end_date = models.DateField(null=True, blank=True)
    construction_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    plumbing_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    plumbing_eng = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="plumbing_engineer",
        null=True,
        blank=True,
    )
    plumbing_start_date = models.DateField(null=True, blank=True)
    plumbing_end_date = models.DateField(null=True, blank=True)
    plumbing_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    electrical_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    electrical_eng = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="electrical_engineer",
        null=True,
        blank=True,
    )
    electrical_start_date = models.DateField(null=True, blank=True)
    electrical_end_date = models.DateField(null=True, blank=True)
    electrical_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    architecture_review = models.CharField(max_length=255, null=True, blank=True)
    architect_reviewer = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="architecture_reviewer",
        null=True,
        blank=True,
    )
    construction_review = models.CharField(max_length=255, null=True, blank=True)
    construction_reviewer = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="construction_reviewer",
        null=True,
        blank=True,
    )
    plumbing_review = models.CharField(max_length=255, null=True, blank=True)
    plumbing_reviewer = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="plumbing_reviewer",
        null=True,
        blank=True,
    )
    electrical_review = models.CharField(max_length=255, null=True, blank=True)
    electrical_reviewer = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="electrical_reviewer",
        null=True,
        blank=True,
    )
    client_received_review_copy_date = models.DateField(null=True, blank=True)
    received_review_copy_from_client_date = models.DateField(null=True, blank=True)
    architecture_notes = models.CharField(max_length=255, null=True, blank=True)
    noted_fields = models.CharField(max_length=100, null=True, blank=True)
    corrector = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name="corrector",
        null=True,
        blank=True,
    )
    corrector_date = models.DateField(null=True, blank=True)
    receive_final_copy_date = models.DateField(null=True, blank=True)

    # typeof_follow_up = models.CharField(max_length=100, choices=FollowUpTypes.choices, null=True, blank=True)
    investor_affiliation = models.CharField(max_length=100, null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sketch_design_progress_status = models.CharField(
        max_length=100, choices=DesignStatus.choices, null=True, blank=True
    )
    plan_delivery_date = models.DateField(null=True, blank=True)

    # created_at = models.DateTimeField(null=True, blank=True)
    moved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.project_name == None:
            return ""
        return self.project_name


@deconstructible
class PathAndRename:
    def __call__(self, instance, filename):
        return f"attachments/{instance.type}s/{filename}"


class Attachment(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(
        max_length=100, choices=AttachmentTypes.choices, null=False, blank=False
    )
    attachment = models.FileField(upload_to=PathAndRename(), null=False, blank=False)
    uploaded_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )
    uploaded_for = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True
    )
    uploaded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.title == None:
            return ""
        return self.title


class Comment(models.Model):
    # title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    written_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to="attachments/", null=True, blank=True)
    written_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=False, blank=False
    )
    written_for = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True
    )

    # def __str__(self):
    #     if self.title == None:
    #         return ""
    #     return self.title


class TableView(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )
    stage = models.CharField(
        max_length=100, choices=Stages.choices, null=False, blank=False
    )
    view = models.JSONField(null=True, blank=True)


class BaladyProject(models.Model):
    global_id = models.IntegerField(null=True, blank=True)

    stage = models.CharField(
        max_length=100, choices=BaladyStages.choices, null=False, blank=False
    )

    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        Client,
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="balady_projects",
        null=False,
        blank=False,
    )
    request_type = models.CharField(
        max_length=100, choices=BaladyRequestTypes.choices, null=False, blank=False
    )
    request_review = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    transaction_stop_reason = models.CharField(max_length=255, null=True, blank=True)
    technical_report = models.CharField(
        max_length=255, choices=Status.choices, null=True, blank=True
    )
    building_inspection_date = models.DateField(null=True, blank=True)
    request_ready_date = models.DateField(null=True, blank=True)
    approval_date = models.DateField(null=True, blank=True)
    is_eng_needed = models.BooleanField(null=True, blank=True)
    sorting_purpose = models.CharField(max_length=255, null=True, blank=True)
    request_submission = models.JSONField(null=True, blank=True)
    municipality_visit = models.JSONField(null=True, blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    moved_at = models.DateTimeField(auto_now_add=True)
    
    # sensitive data
    s_history = models.JSONField(null=True, blank=True, default=list)

    class Meta:
        ordering = ["moved_at"]


class LandSurveyProject(models.Model):
    global_id = models.IntegerField(null=True, blank=True)
    stage = models.CharField(
        max_length=100, choices=LandSurveyStages.choices, null=False, blank=False
    )
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        Client,
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="land_survey_projects",
        null=False,
        blank=False,
    )
    location_visit = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    location_visit_date = models.DateField(null=True, blank=True)
    protocol_number = models.IntegerField(null=True, blank=True)
    transaction_review = models.CharField(max_length=255, null=True, blank=True)
    protocol_purpose = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    survey_report_issuance = models.CharField(max_length=100, null=True, blank=True)


class SortingDeedsProject(models.Model):
    global_id = models.IntegerField(null=True, blank=True)
    stage = models.CharField(
        max_length=100, choices=SortingDeedsStages.choices, null=False, blank=False
    )
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        Client,
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="sorting_deeds_projects",
        null=False,
        blank=False,
    )
    case_study = models.CharField(max_length=100, null=True, blank=True)
    spatial_inspection = models.CharField(max_length=100, null=True, blank=True)
    transaction_upload = models.CharField(max_length=100, null=True, blank=True)
    urban_planning_review = models.CharField(max_length=100, null=True, blank=True)
    issue_bill = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    accounting = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=100, null=True, blank=True)


class GlobalID(models.Model):
    design_id = models.OneToOneField(Project, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    balady_id = models.OneToOneField(BaladyProject, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    sorting_id = models.OneToOneField(SortingDeedsProject, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    land_id = models.OneToOneField(LandSurveyProject, on_delete=models.SET_NULL, null=True, blank=True, unique=True)