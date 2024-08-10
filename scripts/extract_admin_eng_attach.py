import json

balady = {
    "issue_license": {
        "administrative": [
            "land_survey",
            "approved_contractor",
            "engineering_supervision",
        ],
        "engineering": [
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
    },
    "survey_decision": {
        "administrative": [
            "identity",
            "deed",
            "land_survey",
        ],
        "engineering": [],
    },
    "convert_license_to_electronic": {
        "administrative": [
            "identity",
            "deed",
            "old_license",
            "approved_plan",
            "building_pictures",
        ],
        "engineering": [],
    },
    "restoration_license": {
        "administrative": [
            "identity",
            "deed",
            "e_license",
            "approved_plan",
            "container_contract",
            "owner_authorize",
        ],
        "engineering": [
            "technical_report",
        ],
    },
    "add_modify_components_license": {
        "administrative": [
            "identity",
            "deed",
            "e_license",
            "approved_plan",
        ],
        "engineering": [
            "construction_plan",
            "architecture_plan",
            "general_location",
            "facade_picture",
        ],
    },
    "construction_completion_certificate": {
        "administrative": [
            "e_license",
            "building_pictures",
            "owner_authorize",
        ],
        "engineering": [
            "technical_report",
        ],
    },
    "license_separation": {
        "administrative": [
            "identity",
            "deed",
            "e_license_before_sort",
            "coordinate_certificate",
        ],
        "engineering": [
            "architecture_plan",
            "construction_plan",
        ],
    },
    "license_renewal": {
        "administrative": [
            "e_license",
            "architecture_plan",
        ],
        "engineering": [],
    },
    "demolition_license": {
        "administrative": [
            "identity",
            "deed",
            "demolition_letters",
            "coordinate_certificate",
            "architecture_plan",
        ],
        "engineering": [],
    },
    "ownership_license_transfer": {
        "administrative": [
            "e_license",
            "architecture_plan",
        ],
        "engineering": [],
    },
    "service_card": {
        "administrative": [
            "identity",
            "deed",
            "license",
            "architecture_plan",
            "coordinate_certificate_electricity",
        ],
        "engineering": [
            "determine_exert_type",
            "counter_location",
        ],
    },
    "loading_certificate": {
        "administrative": [
            "identity",
            "deed",
            "license",
            "owner_sign_loads",
        ],
        "engineering": [
            "determine_exert_type",
            "standing_cutter_capacity",
            "cutter_capacity_after_strengthening",
            "existing_loads",
            "strengthening_reason",
        ],
    },
    "components_form": {
        "administrative": [
            "deed",
            "license",
            "architecture_plan",
        ],
        "engineering": [],
    },
    "quantity_sorting": {
        "administrative": [
            "complete_plans",
            "request_purpose",
        ],
        "engineering": [],
    },
}

admin_list = []
eng_list = []

for key in balady:
    admin_list = admin_list + balady[key]["administrative"]
    eng_list = eng_list + balady[key]["engineering"]
    
admin_list = list(set(admin_list))
eng_list = list(set(eng_list))

print(f"{admin_list=}")
print(f"{eng_list=}")
