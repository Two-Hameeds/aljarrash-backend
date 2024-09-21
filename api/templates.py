from .models import (
    ReceptionProject,
    DesignProject,
    BaladyProject,
    LandSurveyProject,
    SortingDeedsProject,
    QatariProject,
    SupervisionProject,
)

ATTACHMENT_TEMPLATES = {
    "reception": {
        "model": ReceptionProject,
    },
    "design": {
        "new": {
            "entertaining": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "agricultural": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "residential_commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "civil_defense",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "civil_defense",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "residential": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
        },
        "addition": {
            "entertaining": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "plan",
                "building_pictures",
            ],
            "agricultural": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "plan",
                "building_pictures",
            ],
            "residential_commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "plan",
                "building_pictures",
            ],
            "commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "civil_defense",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "residential": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "plan",
                "building_pictures",
            ],
        },
        "add_floors": {
            "entertaining": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "load_bearing_certificate",
                "plan",
                "building_pictures",
            ],
            "agricultural": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "load_bearing_certificate",
                "plan",
                "building_pictures",
            ],
            "residential_commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "load_bearing_certificate",
                "plan",
                "building_pictures",
            ],
            "commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "civil_defense",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "residential": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "load_bearing_certificate",
                "plan",
                "building_pictures",
            ],
        },
        "restoration": {
            "entertaining": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "report",
                "container_contract",
                "plan",
                "building_pictures",
            ],
            "agricultural": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "report",
                "container_contract",
                "plan",
                "building_pictures",
            ],
            "residential_commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "report",
                "container_contract",
                "plan",
                "building_pictures",
            ],
            "commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "civil_defense",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "residential": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "report",
                "container_contract",
                "plan",
                "building_pictures",
            ],
        },
        "destruction": {
            "entertaining": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "coordinate_certificate",
                "technical_report",
                "demolition_letters",
                "civil_defense",
                "water_authority",
            ],
            "agricultural": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "coordinate_certificate",
                "technical_report",
                "demolition_letters",
                "civil_defense",
                "water_authority",
            ],
            "residential_commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "coordinate_certificate",
                "technical_report",
                "demolition_letters",
                "civil_defense",
                "water_authority",
            ],
            "commercial": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "soil_test",
                "civil_defense",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "residential": [
                "deed",
                "identity",
                "land_survey",
                "client_form",
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "old_license",
                "coordinate_certificate",
                "technical_report",
                "demolition_letters",
                "civil_defense",
                "water_authority",
            ],
        },
        "constants": {
            "type_1": [  # primary
                "deed",
                "report",
                "identity",
                "container_contract",
                "plan",
                "load_bearing_certificate",
                "location_certificate",
                "land_survey",
                "soil_test",
                "coordinate_certificate",
                "demolition_letters",
                "client_form",
                "old_license",
                "civil_defense",
                "water_authority",
            ],
            "type_2": [  # secondary
                "technical_report",
                "projections_approval",
                "facade_approval",
                "columns_approval",
                "ac_approval",
            ],
            "type_3": [  # final
                "architecture_plan",
                "construction_plan",
                "plumbing_plan",
                "electrical_plan",
                "energy_efficiency_plan",
                "civil_defense",
            ],
        },
        "model": DesignProject,
    },
    "balady": {
        "issue_license": [
            "land_survey",
            "approved_contractor",
            "engineering_supervision",
            "general_location",
            "electrical_service_card",
            "architecture_plan",
            "construction_plan",
            "spaces_table",
            "soil_test",
            "facade_picture",
            "energy_efficiency_plan",
            "civil_defense",
        ],
        "survey_decision": [
            "identity",
            "deed",
            "land_survey",
        ],
        "convert_license_to_electronic": [
            "identity",
            "deed",
            "old_license",
            "approved_plan",
            "building_pictures",
        ],
        "restoration_license": [
            "identity",
            "deed",
            "e_license",
            "approved_plan",
            "container_contract",
            "owner_authorize",
            "technical_report",
        ],
        "add_modify_components_license": [
            "identity",
            "deed",
            "e_license",
            "approved_plan",
            "construction_plan",
            "architecture_plan",
            "general_location",
            "facade_picture",
        ],
        "construction_completion_certificate": [
            "e_license",
            "building_pictures",
            "owner_authorize",
            "technical_report",
        ],
        "license_separation": [
            "identity",
            "deed",
            "e_license_before_sort",
            "coordinate_certificate",
            "architecture_plan",
            "construction_plan",
        ],
        "license_renewal": [
            "e_license",
            "architecture_plan",
        ],
        "demolition_license": [
            "identity",
            "deed",
            "demolition_letters",
            "coordinate_certificate",
            "architecture_plan",
        ],
        "ownership_license_transfer": [
            "e_license",
            "architecture_plan",
        ],
        "service_card": [
            "identity",
            "deed",
            "license",
            "architecture_plan",
            "coordinate_certificate_electricity",
            "determine_exert_type",
            "counter_location",
        ],
        "loading_certificate": [
            "identity",
            "deed",
            "license",
            "owner_sign_loads",
            "determine_exert_type",
            "standing_cutter_capacity",
            "cutter_capacity_after_strengthening",
            "existing_loads",
            "strengthening_reason",
        ],
        "components_form": [
            "deed",
            "license",
            "architecture_plan",
        ],
        "quantity_sorting": [
            "complete_plans",
            "request_purpose",
        ],
        "constants": {
            "type_1": [  # administrative
                "e_license",
                "demolition_letters",
                "owner_authorize",
                "request_purpose",
                "approved_plan",
                "approved_contractor",
                "coordinate_certificate",
                "coordinate_certificate_electricity",
                "container_contract",
                "identity",
                "old_license",
                "license",
                "building_pictures",
                "deed",
                "e_license_before_sort",
                "engineering_supervision",
                "complete_plans",
                "land_survey",
                "owner_sign_loads",
            ],
            "type_2": [  # engineering
                "architecture_plan",
                "construction_plan",
                "soil_test",
                "counter_location",
                "cutter_capacity_after_strengthening",
                "standing_cutter_capacity",
                "existing_loads",
                "strengthening_reason",
                "general_location",
                "technical_report",
                "spaces_table",
                "architecture_plan",
                "determine_exert_type",
                "electrical_service_card",
                "civil_defense",
                "facade_picture",
                "energy_efficiency_plan",
            ],
        },
        "model": BaladyProject,
    },
    "land_survey": {
        "required": [
            "general_location",
            "building_pictures",
            "deed",
            "plan",
        ],
        "constants": {
            "type_1": [
                "general_location",
                "building_pictures",
                "deed",
                "plan",
            ],
        },
        "model": LandSurveyProject,
    },
    "sorting_deeds": {
        "required": [
            "deed",
            "identity",
            "approved_plan",
            "license",
            "land_survey",
        ],
        "constants": {
            "type_1": [
                "deed",
                "identity",
                "approved_plan",
                "license",
                "land_survey",
            ],
        },
        "model": SortingDeedsProject,
    },
    "qatari": {
        "required": [
            "general_location",
            "building_pictures",
            "deed",
            "plan",
        ],
        "constants": {
            "type_1": [
                "general_location",
                "building_pictures",
                "deed",
                "plan",
            ],
        },
        "model": QatariProject,
    },
    "supervision": {
        "required": [
            "complete_plans",
        ],
        "constants": {
            "type_1": [  # administrative
                "e_license",
                "demolition_letters",
                "owner_authorize",
                "request_purpose",
                "approved_plan",
                "approved_contractor",
                "coordinate_certificate",
                "coordinate_certificate_electricity",
                "container_contract",
                "identity",
                "old_license",
                "license",
                "building_pictures",
                "deed",
                "e_license_before_sort",
                "engineering_supervision",
                "complete_plans",
                "land_survey",
                "owner_sign_loads",
            ],
            "type_2": [  # engineering
                "architecture_plan",
                "construction_plan",
                "soil_test",
                "counter_location",
                "cutter_capacity_after_strengthening",
                "standing_cutter_capacity",
                "existing_loads",
                "strengthening_reason",
                "general_location",
                "technical_report",
                "spaces_table",
                "architecture_plan",
                "determine_exert_type",
                "electrical_service_card",
                "civil_defense",
                "facade_picture",
                "energy_efficiency_plan",
            ],
        },
        "model": SupervisionProject,
    },
}
