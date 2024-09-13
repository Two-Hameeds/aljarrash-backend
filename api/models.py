from django.db import models
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import AbstractUser

from .choices import (
    ProjectTypes,
    UseTypes,
    Status,
    DesignStatus,
    DesignStages,
    AttachmentTypes,
    BaladyStages,
    LandSurveyStages,
    SortingDeedsStages,
    QatariStages,
    SupervisionStages,
    SupervisionTypes,
)


# TODO: rename to projectModelManager
# Models Managers
class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("moved_at")


# Projects Models
class ReceptionProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
        on_delete=models.CASCADE,
        related_name="reception_projects",
        null=False,
        blank=False,
    )
    notes = models.CharField(max_length=255, null=True, blank=True)


class DesignProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )
    # essential info
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
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
        max_length=100, choices=DesignStages.choices, null=False, blank=False
    )

    # attachments
    required_attachments = models.JSONField(null=True, blank=True)

    design_eng = models.ForeignKey(
        "Employee",
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

    # sensitive fields
    s_project_value = models.FloatField(null=True, blank=True)
    s_payments = models.JSONField(null=True, blank=True, default=list)
    s_modification_price = models.FloatField(null=True, blank=True)

    def s_paid(self):
        paid = sum(float(payment["amount"]) for payment in self.s_payments)
        if self.s_project_value:
            return f"{int(paid / float(self.s_project_value) * 100)}%"
        return "0%"

    architecture_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    architect = models.ForeignKey(
        "Employee",
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
        "Employee",
        on_delete=models.SET_NULL,
        related_name="construction_engineer",
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
        "Employee",
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
        "Employee",
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
        "Employee",
        on_delete=models.SET_NULL,
        related_name="architecture_reviewer",
        null=True,
        blank=True,
    )
    construction_review = models.CharField(max_length=255, null=True, blank=True)
    construction_reviewer = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        related_name="construction_reviewer",
        null=True,
        blank=True,
    )
    plumbing_review = models.CharField(max_length=255, null=True, blank=True)
    plumbing_reviewer = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        related_name="plumbing_reviewer",
        null=True,
        blank=True,
    )
    electrical_review = models.CharField(max_length=255, null=True, blank=True)
    electrical_reviewer = models.ForeignKey(
        "Employee",
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
        "Employee",
        on_delete=models.SET_NULL,
        related_name="corrector",
        null=True,
        blank=True,
    )
    corrector_date = models.DateField(null=True, blank=True)
    receive_final_copy_date = models.DateField(null=True, blank=True)

    investor_affiliation = models.CharField(max_length=100, null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sketch_design_progress_status = models.CharField(
        max_length=100, choices=DesignStatus.choices, null=True, blank=True
    )
    plan_delivery_date = models.DateField(null=True, blank=True)

    moved_at = models.DateTimeField(auto_now_add=True)

    objects = ProjectManager()

    def __str__(self):
        if self.project_name == None:
            return ""
        return self.project_name

    class Meta:
        ordering = ["moved_at"]


class BaladyProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )

    stage = models.CharField(
        max_length=100, choices=BaladyStages.choices, null=False, blank=False
    )

    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="balady_projects",
        null=False,
        blank=False,
    )
    request_types = models.JSONField(
        max_length=100, null=False, blank=False, default=list
    )

    supervisor = models.ForeignKey(
        "Employee",
        on_delete=models.PROTECT,
        related_name="balady_supervisor",
        null=True,
        blank=True,
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
    request_submissions = models.JSONField(null=True, blank=True, default=list)
    municipality_visits = models.JSONField(null=True, blank=True, default=list)

    moved_at = models.DateTimeField(auto_now_add=True)

    record_number = models.CharField(max_length=100, null=True, blank=True)

    # attachments
    required_attachments = models.JSONField(null=True, blank=True, default=list)

    # sensitive data
    s_project_value = models.FloatField(null=True, blank=True)
    s_payments = models.JSONField(default=list)

    def s_paid(self):
        paid = sum(float(payment["amount"]) for payment in self.s_payments)
        if self.s_project_value:
            return f"{int(paid / float(self.s_project_value) * 100)}%"
        return "0%"

    objects = ProjectManager()

    class Meta:
        ordering = ["moved_at"]


class LandSurveyProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )

    stage = models.CharField(
        max_length=100, choices=LandSurveyStages.choices, null=False, blank=False
    )
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="land_survey_projects",
        null=False,
        blank=False,
    )

    supervisor = models.ForeignKey(
        "Employee",
        on_delete=models.PROTECT,
        related_name="land_survey_supervisor",
        null=True,
        blank=True,
    )

    location_visit = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    location_visit_date = models.DateField(null=True, blank=True)
    record_number = models.CharField(null=True, blank=True)
    transaction_review = models.CharField(max_length=255, null=True, blank=True)
    record_purpose = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    survey_report_issuance = models.CharField(max_length=100, null=True, blank=True)
    required_attachments = models.JSONField(null=True, blank=True, default=list)

    moved_at = models.DateTimeField(auto_now_add=True)

    # sensitive data
    s_project_value = models.FloatField(null=True, blank=True)
    s_payments = models.JSONField(default=list)

    def s_paid(self):
        paid = sum(float(payment["amount"]) for payment in self.s_payments)
        if self.s_project_value:
            return f"{int(paid / float(self.s_project_value) * 100)}%"
        return "0%"

    objects = ProjectManager()

    class Meta:
        ordering = ["moved_at"]


class SortingDeedsProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )

    stage = models.CharField(
        max_length=100, choices=SortingDeedsStages.choices, null=False, blank=False
    )
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="sorting_deeds_projects",
        null=False,
        blank=False,
    )

    supervisor = models.ForeignKey(
        "Employee",
        on_delete=models.PROTECT,
        related_name="sorting_deeds_supervisor",
        null=True,
        blank=True,
    )

    case_study = models.CharField(max_length=100, null=True, blank=True)
    spatial_inspection = models.CharField(max_length=100, null=True, blank=True)
    transaction_upload = models.CharField(max_length=100, null=True, blank=True)
    urban_planning_review = models.CharField(max_length=100, null=True, blank=True)
    issue_bill = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    accounting = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=100, null=True, blank=True)

    moved_at = models.DateTimeField(auto_now_add=True)

    required_attachments = models.JSONField(null=True, blank=True, default=list)

    # sensitive data
    s_project_value = models.FloatField(null=True, blank=True)
    s_payments = models.JSONField(default=list)

    def s_paid(self):
        paid = sum(float(payment["amount"]) for payment in self.s_payments)
        if self.s_project_value:
            return f"{int(paid / float(self.s_project_value) * 100)}%"
        return "0%"

    objects = ProjectManager()

    class Meta:
        ordering = ["moved_at"]


class QatariProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )

    stage = models.CharField(
        max_length=100, choices=QatariStages.choices, null=False, blank=False
    )
    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
        to_field="phone",
        on_delete=models.CASCADE,
        related_name="qatary_projects",
        null=False,
        blank=False,
    )

    supervisor = models.ForeignKey(
        "Employee",
        on_delete=models.PROTECT,
        related_name="qatari_supervisor",
        null=True,
        blank=True,
    )

    location_visit = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    location_visit_date = models.DateField(null=True, blank=True)
    record_number = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    transaction_reviewer = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        related_name="qatary_projects_reviewer",
        null=True,
        blank=True,
    )
    record_purpose = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(
        max_length=100, choices=Status.choices, null=True, blank=True
    )
    land_survey_issuance = models.CharField(max_length=100, null=True, blank=True)

    moved_at = models.DateTimeField(auto_now_add=True)

    required_attachments = models.JSONField(null=True, blank=True, default=list)

    # sensitive data
    s_project_value = models.FloatField(null=True, blank=True)
    s_payments = models.JSONField(default=list)

    def s_paid(self):
        paid = sum(float(payment["amount"]) for payment in self.s_payments)
        if self.s_project_value:
            return f"{int(paid / float(self.s_project_value) * 100)}%"
        return "0%"

    objects = ProjectManager()

    class Meta:
        ordering = ["moved_at"]


class SupervisionProject(models.Model):
    global_id = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, null=True, blank=True
    )

    project_name = models.CharField(max_length=100, null=False, blank=False)
    client_phone = models.ForeignKey(
        "Client",
        on_delete=models.CASCADE,
        related_name="provision_projects",
        null=False,
        blank=False,
    )

    stage = models.CharField(
        max_length=100, choices=SupervisionStages.choices, null=False, blank=False
    )

    use_type = models.CharField(
        max_length=100, choices=UseTypes.choices, null=True, blank=True
    )
    supervision_type = models.CharField(
        max_length=100, choices=SupervisionTypes.choices, null=True, blank=True
    )
    contract_date = models.DateField(null=True, blank=True)
    land_number = models.CharField(max_length=100, null=True, blank=True)
    plan_number = models.CharField(max_length=100, null=True, blank=True)
    project_location = models.CharField(max_length=100, null=True, blank=True)
    floors_number = models.SmallIntegerField(null=True, blank=True)
    visits = models.JSONField(null=True, blank=True, default=list)
    supervisor = models.ForeignKey(
        "Employee",
        on_delete=models.PROTECT,
        related_name="provision_supervisor",
        null=True,
        blank=True,
    )
    investor_affiliation = models.CharField(max_length=100, null=True, blank=True)

    required_attachments = models.JSONField(null=True, blank=True, default=list)

    moved_at = models.DateTimeField(auto_now_add=True)

    # sensitive data
    s_project_value = models.FloatField(null=True, blank=True)
    s_payments = models.JSONField(default=list)

    def s_paid(self):
        paid = sum(float(payment["amount"]) for payment in self.s_payments)
        if self.s_project_value:
            return f"{int(paid / float(self.s_project_value) * 100)}%"
        return "0%"

    objects = ProjectManager()

    class Meta:
        ordering = ["moved_at"]


# Projects Related Models
class History(models.Model):
    user = models.ForeignKey("Employee", on_delete=models.CASCADE, related_name="history")
    project = models.ForeignKey("GlobalID", on_delete=models.CASCADE, related_name="history")
    action = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    previous_stage = models.CharField(max_length=100, null=True, blank=True, default=None)
    new_stage = models.CharField(max_length=100, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

class Visit(models.Model):
    employee = models.ForeignKey(
        "Employee", on_delete=models.CASCADE, related_name="visits"
    )
    date = models.DateField()
    purpose = models.CharField(max_length=100, null=True, blank=True)
    note = models.CharField(max_length=300, null=True, blank=True)
    attachment = models.FileField(
        upload_to="visits_attachments/", null=True, blank=True
    )
    visited_for = models.ForeignKey(
        "GlobalID", on_delete=models.CASCADE, related_name="visits"
    )


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    paid_for = models.ForeignKey("GlobalID", on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField(blank=True, null=True)
    stage = models.CharField(max_length=100)


class TableView(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    employee = models.ForeignKey(
        "Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    stage = models.CharField(
        max_length=100, choices=DesignStages.choices, null=False, blank=False
    )
    view = models.JSONField(null=True, blank=True)


class Comment(models.Model):
    content = models.TextField(max_length=255, null=True, blank=True)
    written_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to="attachments/", null=True, blank=True)
    written_by = models.ForeignKey(
        "Employee", on_delete=models.CASCADE, null=False, blank=False
    )
    written_for = models.ForeignKey(
        "GlobalID",
        on_delete=models.SET_NULL,
        related_name="comments",
        null=True,
        blank=True,
    )


@deconstructible
class PathAndRename:
    def __call__(self, instance, filename):
        return f"attachments/{instance.type}s/{filename}"


class Attachment(models.Model):
    type = models.CharField(
        max_length=100, choices=AttachmentTypes.choices, null=False, blank=False
    )
    attachment = models.FileField(upload_to=PathAndRename(), null=False, blank=False)
    uploaded_by = models.ForeignKey(
        "Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    uploaded_for = models.ForeignKey(
        "GlobalID",
        on_delete=models.SET_NULL,
        related_name="attachments",
        null=True,
        blank=True,
    )
    uploaded_at = models.DateTimeField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.title == None:
            return ""
        return self.title


# Other Models
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


class GlobalID(models.Model):
    design = models.OneToOneField(
        DesignProject, on_delete=models.SET_NULL, null=True, blank=True, unique=True
    )
    balady = models.OneToOneField(
        BaladyProject, on_delete=models.SET_NULL, null=True, blank=True, unique=True
    )
    sorting = models.OneToOneField(
        SortingDeedsProject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        unique=True,
    )
    land = models.OneToOneField(
        LandSurveyProject, on_delete=models.SET_NULL, null=True, blank=True, unique=True
    )
    qatari = models.OneToOneField(
        QatariProject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        unique=True,
    )
    supervision = models.OneToOneField(
        SupervisionProject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        unique=True,
    )
