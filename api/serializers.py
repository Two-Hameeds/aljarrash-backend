from rest_framework import serializers

from django.contrib.auth.models import Group
from .models import (
    Employee,
    Client,
    DesignProject,
    Attachment,
    Comment,
    TableView,
    BaladyProject,
    LandSurveyProject,
    SortingDeedsProject,
    QatariOfficeProject,
    GlobalID,
    Payment,
)
from django.utils import timezone
from .templates import ATTACHMENT_TEMPLATES


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    def to_representation(self, instance):
        default = super().to_representation(instance)

        default["name"] = self.get_name(instance)

        return super().to_representation(instance)

    def update(self, instance, validated_data):
        password_changed = not validated_data.get("password") == instance.password
        updated_instance = super().update(instance, validated_data)
        if password_changed:
            updated_instance.set_password(updated_instance.password)
            updated_instance.save()
        return updated_instance

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = "__all__"

    def get_name(self, obj):
        if obj.first_name == "" and obj.last_name == "":
            return None
        return obj.first_name + " " + obj.last_name


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


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
        if str(self.context["request"].user) == "AnonymousUser":
            validated_data["uploaded_by"] = None
        else:
            validated_data["uploaded_by"] = self.context["request"].user
        return super().create(validated_data)

    class Meta:
        model = Attachment
        fields = "__all__"


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


# Projects Serializers
class DesignProjectSerializer(serializers.ModelSerializer):
    s_paid = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    def get_filtered_fields(self, default):
        user = self.context["request"].user
        stage = self.context["request"].query_params.get("stage")
        table_view = self.context["request"].query_params.get("table_view")

        if not stage and not table_view:
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
        table_view_data.insert(1, "global_id")
        table_view_data.insert(2, "s_paid")

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
        # validated_data["moved_at"] = timezone.now()

        # if self.context["request"]:
        #     validated_data["s_history"] = [
        #         {
        #             "created_by": str(self.context["request"].user),
        #             "created_at": str(timezone.now()),
        #             "created_in": validated_data["stage"],
        #         }
        #     ]

        project_type = validated_data["project_type"]
        use_type = validated_data["use_type"]

        validated_data["required_attachments"] = ATTACHMENT_TEMPLATES["design"][
            project_type
        ][use_type]

        result = super().create(validated_data)
        if validated_data.get("global_id") == None:
            global_id, created = GlobalID.objects.get_or_create(design=result)
            result.global_id = global_id
            result.save()

        return result

    def get_attachments_status(self, obj):
        if not self.context:
            return {}

        constants = ATTACHMENT_TEMPLATES["design"]["constants"]

        attachments_list = list(Attachment.objects.filter(uploaded_for=obj.id))
        primary = []
        secondary = []
        final = []

        for attachment in attachments_list:
            if attachment.type in constants["type_1"]:
                if attachment.type not in primary:
                    primary.append(attachment.type)
            elif attachment.type in constants["type_2"]:
                if attachment.type not in secondary:
                    secondary.append(attachment.type)
            elif attachment.type in constants["type_3"]:
                if attachment.type not in final:
                    final.append(attachment.type)

        required_primary = [
            primary_instance
            for primary_instance in constants["type_1"]
            if primary_instance in obj.required_attachments
        ]
        required_secondary = [
            secondary_instance
            for secondary_instance in constants["type_2"]
            if secondary_instance in obj.required_attachments
        ]
        required_final = [
            final_instance
            for final_instance in constants["type_3"]
            if final_instance in obj.required_attachments
        ]
        primary_status = len(required_primary) == len(primary)
        secondary_status = len(required_secondary) == len(secondary)
        final_status = len(required_final) == len(final)
        if primary_status and secondary_status and final_status:
            return 3
        elif primary_status and secondary_status:
            return 2
        elif primary_status:
            return 1
        else:
            return 0

    def to_representation(self, instance):
        default = super().to_representation(instance)

        default["attachments_status"] = self.get_attachments_status(instance)

        default.pop("required_attachments")
        if self.context and self.context["request"].user.is_superuser:
            default.pop("s_payments")

        if instance.global_id == None:
            global_id, created = GlobalID.objects.get_or_create(design=instance)
            instance.global_id = global_id
            instance.save()

        return default

    def get_s_paid(self, obj):
        return obj.s_paid()

    class Meta:
        model = DesignProject
        fields = "__all__"


class BaladyProjectSerializer(serializers.ModelSerializer):
    s_paid = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

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

        # if self.context["request"]:
        #     validated_data["s_history"] = [
        #         {
        #             "created_by": str(self.context["request"].user),
        #             "created_at": str(timezone.now()),
        #             "created_in": validated_data["stage"],
        #         }
        #     ]
        request_types = validated_data["request_types"]
        required_attachments = []
        for request_type in request_types:
            required_attachments = (
                required_attachments + ATTACHMENT_TEMPLATES["balady"][request_type]
            )

        validated_data["required_attachments"] = list(set(required_attachments))

        result = super().create(validated_data)
        if validated_data.get("global_id") == None:
            global_id, created = GlobalID.objects.get_or_create(balady=result)
            result.global_id = global_id
            result.save()
        return result

    def attachments_status(self, instance):
        attach_count = (
            Attachment.objects.filter(
                uploaded_for=instance.global_id, type__in=instance.required_attachments
            )
            .distinct("type")
            .count()
        )

        attach_status = 0

        try:
            attach_status = int(attach_count / len(instance.required_attachments) * 3)
        except:
            pass

        return attach_status

    def to_representation(self, instance):
        default = super().to_representation(instance)

        default["attachments_status"] = self.attachments_status(instance)

        default["comments_count"] = Comment.objects.filter(
            written_for=instance.global_id
        ).count()

        # default.pop("required_attachments")
        if self.context:  # and self.context["request"].user.is_superuser:
            default.pop("s_payments")

        return default

    def get_s_paid(self, obj):
        return obj.s_paid()

    class Meta:
        model = BaladyProject
        fields = "__all__"


class LandSurveyProjectSerializer(serializers.ModelSerializer):
    s_paid = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

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
        validated_data["required_attachments"] = ATTACHMENT_TEMPLATES["land_survey"][
            "required"
        ]
        result = super().create(validated_data)
        if validated_data.get("global_id") == None:
            global_id, created = GlobalID.objects.get_or_create(land=result)
            result.global_id = global_id
            result.save()
        return result

    def get_s_paid(self, obj):
        return obj.s_paid()

    class Meta:
        model = LandSurveyProject
        fields = "__all__"


class SortingDeedsProjectSerializer(serializers.ModelSerializer):
    s_paid = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

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
        validated_data["required_attachments"] = ATTACHMENT_TEMPLATES["sorting_deeds"][
            "required"
        ]
        result = super().create(validated_data)
        if validated_data.get("global_id") == None:
            global_id, created = GlobalID.objects.get_or_create(sorting=result)
            result.global_id = global_id
            result.save()
        return result

    def get_s_paid(self, obj):
        return obj.s_paid()

    class Meta:
        model = SortingDeedsProject
        fields = "__all__"


class QatariOfficeProjectSerializer(serializers.ModelSerializer):
    s_paid = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        validated_data["required_attachments"] = ATTACHMENT_TEMPLATES["qatari"][
            "required"
        ]
        result = super().create(validated_data)
        if validated_data.get("global_id") == None:
            global_id, created = GlobalID.objects.get_or_create(qatari=result)
            result.global_id = global_id
            result.save()

        return result

    def get_s_paid(self, obj):
        return obj.s_paid()

    class Meta:
        model = QatariOfficeProject
        fields = "__all__"


# Projects Related Serializers
class PaymentsSerializer(serializers.Serializer):
    s_contract = serializers.FileField()
    s_project_value = serializers.FloatField()
    s_payments = serializers.JSONField()


class RequestSubmissionSerializer(serializers.Serializer):
    requests = serializers.ListField()


class MunicipalityVisitSerializer(serializers.Serializer):
    visits = serializers.ListField()


class RequiredAttachmentSerializer(serializers.Serializer):
    required_attachments = serializers.ListField()


# Other Serializers
class GlobalIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalID
        fields = "__all__"


count = 0


class PaymentSerializer(serializers.ModelSerializer):
    # def get_fields(self):
    #     global count
    #     if count == 0:
    #         # Payment.objects.all().delete()
    #         projects = Project.objects.all()
    #         # for project in projects:
    #         #     for payment in project.s_payments:
    #         #         Payment.objects.create(
    #         #             paid_for=project.global_id,
    #         #             amount=payment["amount"],
    #         #             date=payment["date"] if payment["date"] else None,
    #         #             stage=payment["stage"],
    #         #         )

    #     count = count + 1
    #     return super().get_fields()

    class Meta:
        model = Payment
        fields = "__all__"
