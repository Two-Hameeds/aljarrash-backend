from rest_framework import serializers
from .models import (
    Employee,
    Client,
    Project,
    Attachment,
    Comment,
    TableView,
    BaladyProject,
    LandSurveyProject,
    SortingDeedsProject,
    GlobalID,
)
from django.utils import timezone
from pathlib import Path


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    def to_representation(self, instance):
        default = super().to_representation(instance)

        default["name"] = self.get_name(instance)

        return super().to_representation(instance)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        # TODO user_permissions and groups update should be handled individually
        user_permissions = validated_data.pop("user_permissions", None)
        groups = validated_data.pop("groups", None)

        if password is not None and not password == instance.password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    class Meta:
        model = Employee
        fields = "__all__"

    def get_name(self, obj):
        if obj.first_name == "" and obj.last_name == "":
            return None
        return obj.first_name + " " + obj.last_name


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "is_active",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class RemoveTokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["username"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        validated_data["uploaded_at"] = timezone.now()
        return super().create(validated_data)

    class Meta:
        model = Attachment
        fields = "__all__"
        
class RequiredAttachmentSerializer(serializers.Serializer):
    required_attachments = serializers.ListField()

class CommentSerializer(serializers.ModelSerializer):
    written_at = serializers.DateTimeField(read_only=True)
    written_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        validated_data["written_at"] = timezone.now()
        if str(self.context["request"].user) == "AnonymousUser":
            validated_data["written_by"] = None
        else:
            validated_data["written_by"] = self.context["request"].user
        return super().create(validated_data)

    class Meta:
        model = Comment
        fields = "__all__"


class TableViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableView
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(read_only=True)
    history = serializers.JSONField(read_only=True)

    def get_filtered_fields(self, default):
        user = self.context["request"].user
        stage = self.context["request"].query_params.get("current_stage")
        table_view = self.context["request"].query_params.get("table_view")

        if (not stage and not table_view) or (
            stage == "completed_projects" or stage == "inactive_projects"
        ):
            table_view_data = list(default.keys())
        elif stage and table_view:
            table_view_data = TableView.objects.values_list().get(
                stage=stage, name=table_view
            )[4]
        elif stage:
            table_view_data = TableView.objects.values_list().get(
                stage=stage, name="default"
            )[4]
        elif table_view:
            table_view_data = TableView.objects.values_list().get(name=table_view)[4]

        table_view_data.insert(0, "id")

        if not user.is_staff:
            table_view_data = list(
                filter(lambda element: not element.startswith("s_"), table_view_data)
            )

        return {key: default[key] for key in table_view_data if key in default}

    def get_fields(self):
        default = super().get_fields()
        if not self.context:
            return default
        if (
            str(self.context["request"].method) == "POST"
            and self.context["request"].data
        ):
            Client.objects.get_or_create(
                phone=self.context["request"].data["client_phone"]
            )

        filtered_fields = self.get_filtered_fields(default)

        return filtered_fields

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now()
        validated_data["moved_at"] = timezone.now()
        
        # allFilesTypes = [
        #     "contract",
        #     "deed",
        #     "identity",
        #     "land_survey",
        #     "client_form",
        #     "architecture_plan",
        #     "construction_plan",
        #     "plumbing_plan",
        #     "electrical_plan",
        #     "energy_efficiency_plan",
        #     "soil_test",
        #     "civil_defense",
        #     "old_license",
        #     "plan",
        #     "building_pictures",
        #     "load_bearing_certificate",
        #     "report",
        #     "container_contract",
        #     "coordinate_certificate",
        #     "technical_report",
        #     "demolition_letters",
        #     "water_authority",
        # ]

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

        project_type = validated_data["project_type"]
        use_type = validated_data["use_type"]

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

        validated_data["required_attachments"] = required_attachments
        
        result = super().create(validated_data)
        if(validated_data.get("global_id") == None):
            global_id, created  = GlobalID.objects.get_or_create(
                design_id = result
            )
            result.global_id = global_id.id
            result.save()

        return result

    def get_attachments(self, obj):
        if not self.context:
            return {}

        all_primary = [
            "contract",
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
        ]

        all_secondary = {
            "technical_report",
        }

        all_final = [
            "architecture_plan",
            "construction_plan",
            "plumbing_plan",
            "electrical_plan",
            "energy_efficiency_plan",
            "civil_defense",
        ]

        attachments = {}
        attachments_list = list(Attachment.objects.filter(uploaded_for=obj.id))
        primary = []
        secondary = []
        final = []

        for attachment in attachments_list:
            if(attachment.type in all_primary):
                if attachment.type not in primary:
                    primary.append(attachment.type)
            elif(attachment.type in all_secondary):
                if attachment.type not in secondary:
                    secondary.append(attachment.type)
            elif(attachment.type in all_final):
                if attachment.type not in final:
                    final.append(attachment.type)

            if attachment.type not in attachments:
                attachments[attachment.type] = []

            attachments[attachment.type].insert(
                0, self.context["request"].build_absolute_uri(attachment.attachment.url)
            )
        required_primary = [primary_instance for primary_instance in all_primary if primary_instance in obj.required_attachments]
        required_secondary = [secondary_instance for secondary_instance in all_secondary if secondary_instance in obj.required_attachments]
        required_final = [final_instance for final_instance in all_final if final_instance in obj.required_attachments]
        primary_status = len(required_primary) == len(primary)
        secondary_status = len(required_secondary) == len(secondary)
        final_status = len(required_final) == len(final)

        return [attachments, primary_status, secondary_status, final_status]

    def get_comments_count(self, obj_id):
        return Comment.objects.filter(written_for=obj_id).count()

    def to_representation(self, instance):
        default = super().to_representation(instance)

        default["attachments"] = self.get_attachments(instance)[0]
        default["primary_status"] = self.get_attachments(instance)[1]
        default["secondary_status"] = self.get_attachments(instance)[2]
        default["final_status"] = self.get_attachments(instance)[3]
        default["comments_count"] = self.get_comments_count(instance.id)

        return default

    class Meta:
        model = Project
        fields = "__all__"




class BaladyProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    def get_fields(self):
        default = super().get_fields()
        if not self.context:
            return default

        if (
            str(self.context["request"].method) == "POST"
            and self.context["request"].data
        ):
            Client.objects.get_or_create(
                phone=self.context["request"].data["client_phone"]
            )
        return default
    
    def create(self, validated_data):
        result = super().create(validated_data)
        if(validated_data.get("global_id") == None):
            global_id, created  = GlobalID.objects.get_or_create(
                balady_id = result
            )
            result.global_id = global_id.id
            result.save()
        return result

    class Meta:
        model = BaladyProject
        fields = "__all__"


class LandSurveyProjectSerializer(serializers.ModelSerializer):

    def get_fields(self):
        if (
            str(self.context["request"].method) == "POST"
            and self.context["request"].data
        ):
            Client.objects.get_or_create(
                phone=self.context["request"].data["client_phone"]
            )
        return super().get_fields()
    
    def create(self, validated_data):
        result = super().create(validated_data)
        if(validated_data.get("global_id") == None):
            global_id, created  = GlobalID.objects.get_or_create(
                land_id = result
            )
            result.global_id = global_id.id
            result.save()
        return result

    class Meta:
        model = LandSurveyProject
        fields = "__all__"


class SortingDeedsProjectSerializer(serializers.ModelSerializer):

    def get_fields(self):
        if (
            str(self.context["request"].method) == "POST"
            and self.context["request"].data
        ):
            Client.objects.get_or_create(
                phone=self.context["request"].data["client_phone"]
            )
        return super().get_fields()
    
    def create(self, validated_data):
        result = super().create(validated_data)
        if(validated_data.get("global_id") == None):
            global_id, created  = GlobalID.objects.get_or_create(
                sorting_id = result
            )
            result.global_id = global_id.id
            result.save()
        return result

    class Meta:
        model = SortingDeedsProject
        fields = "__all__"

class GlobalIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalID
        fields = "__all__"