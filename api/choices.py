from django.db import models

class ProjectTypes(models.TextChoices):
    Destruction = "destruction"
    Restoration = "restoration"
    AddFloors = "add_floors"
    Addition = "addition"
    New = "new"


class UseTypes(models.TextChoices):
    Entertaining = "entertaining"
    Agricultural = "agricultural"
    ResidentialCommercial = "residential_commercial"
    Commercial = "commercial"
    Residential = "residential"


class Status(models.TextChoices):
    Working_on_it = "Working on it"
    Done = "Done"
    Hold = "Hold"
    Not_required = "Not required"
    Ready = "ready"
    No = "no"


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
    Working_on_it = "Working on it"
    Done = "Done"


class Stages(models.TextChoices):
    Sketch = "sketch"
    Sketch_Review = "sketch_review"
    Approval_Before_Columns = "approval_before_columns"
    Awaiting_Client_Approval = "awaiting_client_approval"
    Execution_Stage = "execution_stage"
    AutoCAD_Review = "autocad_review"
    Ready_to_Print = "ready_to_print"
    Validate_Sign_Review_Copy = "validate_sign_review_copy"
    Ready_to_Collect = "ready_to_collect"
    Client_Received_Copy = "client_received_copy"
    Edit_Client_Notes = "edit_client_notes"
    License_Issuance = "license_issuance"
    Ready_for_Final_Receipt = "ready_for_final_receipt"
    Completed_Projects = "completed_projects"
    Inactive_Projects = "inactive_projects"


class AttachmentTypes(models.TextChoices):
    Contract = "contract"
    Deed = "deed"
    Report = "report"
    Identity = "identity"
    ContainerContract = "container_contract"
    License = "license"
    Plan = "plan"
    OldPlan = "old_plan"
    LoadBearingCertificate = "load_bearing_certificate"
    LocationCertificate = "location_certificate"
    LandSurvey = "land_survey"
    SoilTest = "soil_test"
    CoordinateCertificate = "coordinate_certificate"
    TechnicalReport = "technical_report"
    DemolitionLetters = "demolition_letters"
    Autocad = "autocad"
    ClientForm = "client_form"
    OldLicense = "old_license"
    CivilDefense = "civil_defense"
    WaterAuthority = "water_authority"
    ConstructionPlan = "construction_plan"
    ElectricalPlan = "electrical_plan"
    EnergyEfficiencyPlan = "energy_efficiency_plan"
    PlumbingPlan = "plumbing_plan"
    ArchitecturePlan = "architecture_plan"
    BuildingPictures = "building_pictures"
    Other = "other"


class BaladyStages(models.TextChoices):
    Balady = "balady"
    Service_Card = "service_card"
    Quantity_Sorting = "quantity_sorting"


class BaladyRequestTypes(models.TextChoices):
    Issue_License = "issue_license"
    Convert_License_to_Electronic = "convert_license_to_electronic"
    Restoration_License = "restoration_license"
    Add_Modify_Components_License = "add_modify_components_license"
    Construction_Completion_Certificate = "construction_completion_certificate"

    license_separation = "license_separation"
    license_renewal = "license_renewal"
    demolition_license = "demolition_license"
    ownership_license_transfer = "ownership_license_transfer"
    survey_decision = "survey_decision"
    service_card = "service_card"
    loading_certificate = "loading_certificate"
    components_form = "components_form"
    quantity_sorting = "quantity_sorting"


class LandSurveyStages(models.TextChoices):
    land_survey = "land_survey"
    land_report = "land_report"
    completed_projects = "completed_projects"
    informal_transactions = "informal_transactions"


class SortingDeedsStages(models.TextChoices):
    land_sorting = "land_sorting"
    land_merging = "land_merging"
    housing_sorting = "housing_sorting"
    land_sorting_completed = "land_sorting_completed"
    land_merging_completed = "land_merging_completed"
    housing_sorting_completed = "housing_sorting_completed"
