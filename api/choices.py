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
    Post_Tension = "Post Tension"
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


class DesignStages(models.TextChoices):
    Reception = "reception"
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
    Deleted_Projects = "deleted_projects"


class AttachmentTypes(models.TextChoices):
    # common
    deed = "deed"
    license = "license"
    architecture_plan = "architecture_plan"
    identity = "identity"
    land_survey = "land_survey"
    soil_test = "soil_test"
    coordinate_certificate = "coordinate_certificate"
    technical_report = "technical_report"
    demolition_letters = "demolition_letters"
    old_license = "old_license"
    civil_defense = "civil_defense"
    construction_plan = "construction_plan"
    energy_efficiency_plan = "energy_efficiency_plan"
    building_pictures = "building_pictures"
    container_contract = "container_contract"
    other = "other"
    
    # design
    contract = "contract"
    report = "report"
    plan = "plan"
    old_plan = "old_plan"
    load_bearing_certificate = "load_bearing_certificate"
    location_certificate = "location_certificate"
    autocad = "autocad"
    client_form = "client_form"
    water_authority = "water_authority"
    electrical_plan = "electrical_plan"
    plumbing_plan = "plumbing_plan"
    projections_approval = "projections_approval"
    facade_approval ="facade_approval"
    columns_approval = "columns_approval"
    ac_approval = "ac_approval"
    
    # balady
    complete_plans = "complete_plans"
    request_purpose = "request_purpose"
    determine_exert_type = "determine_exert_type"
    standing_cutter_capacity = "standing_cutter_capacity"
    cutter_capacity_after_strengthening = "cutter_capacity_after_strengthening"
    existing_loads = "existing_loads"
    strengthening_reason = "strengthening_reason"
    owner_sign_loads = "owner_sign_loads"
    counter_location = "counter_location"
    coordinate_certificate_electricity = "coordinate_certificate_electricity"
    e_license = "e_license"
    e_license_before_sort = "e_license_before_sort"
    owner_authorize = "owner_authorize"
    general_location = "general_location"
    facade_picture = "facade_picture"
    approved_plan = "approved_plan"
    electrical_service_card = "electrical_service_card"
    spaces_table = "spaces_table"
    approved_contractor = "approved_contractor"
    engineering_supervision = "engineering_supervision"

class BaladyStages(models.TextChoices):
    Balady = "balady"
    Completed_Balady = "completed_balady"
    Stopped_Balady = "stopped_balady"
    Service_Card = "service_card"
    Completed_Service_Card = "completed_service_card"
    Quantity_Sorting = "quantity_sorting"
    Completed_Quantity_Sorting = "completed_quantity_sorting"
    Deleted_Projects = "deleted_projects"


class BaladyRequestTypes(models.TextChoices):
    issue_license = "issue_license"
    convert_license_to_electronic = "convert_license_to_electronic"
    restoration_license = "restoration_license"
    add_modify_components_license = "add_modify_components_license"
    construction_completion_certificate = "construction_completion_certificate"
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
    completed_land_survey = "completed_land_survey"
    land_report = "land_report"
    completed_land_report = "completed_land_report"
    informal_transactions = "informal_transactions"
    completed_informal_transactions = "completed_informal_transactions"
    deleted_projects = "deleted_projects"


class SortingDeedsStages(models.TextChoices):
    land_sorting = "land_sorting"
    land_merging = "land_merging"
    housing_sorting = "housing_sorting"
    completed_land_sorting = "completed_land_sorting"
    completed_land_merging = "completed_land_merging"
    completed_housing_sorting = "completed_housing_sorting"
    deleted_projects = "deleted_projects"

class QatariStages(models.TextChoices):
    main = "main"
    land_report = "land_report"
    completed_land_survey = "completed_land_survey"
    informal_transactions = "informal_transactions"
    deleted_projects = "deleted_projects"
    

class SupervisionStages(models.TextChoices):
    main = 'main'
    visit_supervision = 'visit_supervision'
    completed_supervision = 'completed_supervision'
    deleted_projects = 'deleted_projects'
    
class SupervisionTypes(models.TextChoices):
    indoor_contract = "indoor_contract"
    outdoor_contract = "outdoor_contract"
    indoor_visits = "indoor_visits"
    outdoor_visits = "outdoor_visits"