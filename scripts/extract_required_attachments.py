common_attachments = [
    "contract",
    "deed",
    "identity",
    "land_survey",
    "client_form",
    "architecture_plan",
    "construction_plan",
    "plumbing_plan",
    "electrical_plan",
    "energy_efficiency_plan",
]

new_residential_commercial = ["soil_test", "civil_defense"]

new_other = ["soil_test"]
addition = ["old_license", "plan", "building_pictures"]
add_floors = [
    "old_license",
    "load_bearing_certificate",
    "plan",
    "building_pictures",
]
restoration = [
    "old_license",
    "report",
    "container_contract",
    "plan",
    "building_pictures",
]
destruction = [
    "old_license",
    "coordinate_certificate",
    "technical_report",
    "demolition_letters",
    "civil_defense",
    "water_authority",
]

required_attachments = common_attachments

project_type = input("project_type: ")
use_type = input("use_type: ")

if project_type == "new":
    if use_type == "residential_commercial":
        required_attachments.extend(new_residential_commercial)
    else:
        required_attachments.extend(new_other)
elif project_type == "addition":
    required_attachments.extend(addition)
elif project_type == "add_floors":
    required_attachments.extend(add_floors)
elif project_type == "restoration":
    required_attachments.extend(restoration)
elif project_type == "destruction":
    required_attachments.extend(destruction)

print(required_attachments)